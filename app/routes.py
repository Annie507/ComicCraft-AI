from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse

from .schemas import PromptRequest
from .ai.gemini_flash import generate_outline
from .ai.gemini_pro import generate_story
from .image_generator import generate_image


router = APIRouter()


@router.get("/")
async def home(request: Request):

    from .main import templates

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


def run_generation(req):

    outline = generate_outline(req)

    story = generate_story(
        outline,
        req
    )

    for panel in outline:

        image = generate_image(
            panel["image_prompt"],
            panel["panel_number"]
        )

        panel["image_url"] = image["image_url"]
        panel["image_path"] = image["image_path"]

    return outline


@router.post("/generate")
async def generate(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    from .main import templates

    try:

        req = PromptRequest(
            story_prompt=story_prompt,
            character_name=character_name,
            setting=setting,
            tone=tone,
            art_style=art_style
        )

        layout = run_generation(req)

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "request": request,
                "layout": layout
            }
        )

    except Exception as exc:

        print("GENERATION ERROR:", repr(exc))

        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={
                "request": request,
                "error": str(exc)
            },
            status_code=500
        )


@router.post("/test-image")
async def test_image(prompt: str = Form(...)):

    try:

        result = generate_image(
            prompt,
            1
        )

        return JSONResponse({
            "success": True,
            "image": result
        })

    except Exception as exc:

        return JSONResponse({
            "success": False,
            "error": str(exc)
        })