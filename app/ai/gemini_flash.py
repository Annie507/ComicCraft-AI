from .config import MAX_PANELS


def generate_outline(req):

    scenes = [
        f"Opening scene: {req.story_prompt}",
        f"The adventure begins: {req.story_prompt}",
        f"An important event happens: {req.story_prompt}",
        f"The main conflict reaches its climax: {req.story_prompt}",
        f"The story reaches a happy ending: {req.story_prompt}",
    ]

    panels = []

    for number in range(1, MAX_PANELS + 1):

        scene = scenes[number - 1]

        image_prompt = f"""
Create one high-quality comic illustration.

Main character: {req.character_name}
Setting: {req.setting}
Tone: {req.tone}
Art style: {req.art_style}

Story:
{req.story_prompt}

Current scene:
{scene}

Requirements:
- Clearly show the main character.
- Clearly show the environment.
- Cinematic composition.
- Consistent character appearance.
- Detailed background.
- Natural lighting.
- No written text.
- No captions.
- No speech bubbles.
"""

        panels.append({
            "panel_number": number,
            "title": f"Scene {number}",
            "scene_description": scene,
            "caption": f"Scene {number}",
            "narration": scene,
            "dialogue": f"{req.character_name}: What happens next?",
            "image_prompt": image_prompt,
        })

    return panels