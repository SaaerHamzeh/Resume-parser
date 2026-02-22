import fitz
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text("text")

    if not text.strip():
        raise ValueError("No readable text found in PDF.")

    return text.strip()
