from pathlib import Path

from fpdf import FPDF


BASE_DIR = Path(__file__).resolve().parent
EXPORT_DIR = BASE_DIR / "static" / "exports"

EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(layout, filename="comiccraft_comic.pdf"):
    """
    Save the generated comic layout as a PDF.
    """

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for panel in layout:
        pdf.add_page()

        title = panel.get("title", "Comic Panel")
        text = panel.get("text", "")
        image_path = panel.get("image_path")

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, str(title), ln=True)

        if image_path:
            image_file = Path(image_path)

            if image_file.exists():
                try:
                    pdf.image(str(image_file), x=15, y=30, w=180)
                    pdf.ln(125)
                except Exception:
                    pdf.ln(10)

        pdf.set_font("Arial", size=11)

        if text:
            safe_text = str(text).encode(
                "latin-1",
                "replace"
            ).decode("latin-1")

            pdf.multi_cell(0, 8, safe_text)

    output_path = EXPORT_DIR / filename

    pdf.output(str(output_path))

    return f"/static/exports/{filename}"