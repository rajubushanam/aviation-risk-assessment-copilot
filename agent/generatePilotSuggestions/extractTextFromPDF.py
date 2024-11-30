import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file and return as a single string."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            text += f"\n--- Page {page_num} ---\n"  # Add page markers for context
            text += page.get_text()  # Extract text from the page
    return text
