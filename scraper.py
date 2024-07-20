import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Example usage
def get_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    return text

if __name__ == "__main__":
    url = 'https://nmit.ac.in'
    url2='https://www.alkimi.org/tokenomics?section=alkimi-exchange'
    url3='https://www.alkimi.org/tokenomics?section=validators'
    path1 = "/Users/abbasbaba/PycharmProjects/hackathon/pd1.pdf"
    extracted_text = extract_text_from_pdf(path1)
    text = get_text_from_url(url)+get_text_from_url(url2)+get_text_from_url(url3)+extracted_text
    file_path = "abs.txt"
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Text has been saved to {file_path}")




