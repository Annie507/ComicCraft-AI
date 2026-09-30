def build_comic_layout(outline, story=None, images=None):

    panels = outline

    if images:
        for i, panel in enumerate(panels):

            if i < len(images):

                image = images[i]

                if isinstance(image, dict):

                    panel["image_url"] = image.get("image_url")
                    panel["image_path"] = image.get("image_path")

    return panels