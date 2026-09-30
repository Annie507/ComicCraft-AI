from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routes import router


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="ComicCraft",
    version="1.0"
)


STATIC_DIR = BASE_DIR / "static"
STATIC_DIR.mkdir(exist_ok=True)

GENERATED_DIR = STATIC_DIR / "generated_images"
GENERATED_DIR.mkdir(exist_ok=True)


app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static"
)


templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


app.include_router(router)


@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "ComicCraft"
    }