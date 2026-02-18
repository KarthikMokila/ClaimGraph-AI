import pdfplumber
from fastapi import UploadFile

async def extract_pages(file: UploadFile):
    pages_text = []

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)
        
    return pages_text