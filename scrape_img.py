from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Example usage
pdf_path = "/Users/abbasbaba/PycharmProjects/hackathon/pd1.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)