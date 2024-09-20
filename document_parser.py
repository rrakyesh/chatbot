import pdfplumber

def parse_document(document_content):
    # Parse PDF content
    with pdfplumber.open(document_content) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
