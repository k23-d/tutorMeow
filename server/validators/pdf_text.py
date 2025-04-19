import fitz  # PyMuPDF

def extract_pdf_text(file_bytes: bytes) -> str:
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        return " ".join([page.get_text() for page in doc])[:3000]
