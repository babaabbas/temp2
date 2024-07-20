import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Get the file name from the URL
        filename = os.path.join(folder, url.split("/")[-1])

        # Write the image to a file
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Could not download {url}. Error: {e}")


# Function to scrape images from a URL
def scrape_images(url, folder="images"):
    # Create the folder if it does not exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags
    images = soup.find_all('img')

    for img in images:
        img_url = img.get('src')
        if img_url:
            # Handle relative URLs
            img_url = urljoin(url, img_url)
            download_image(img_url, folder)


if __name__ == "__main__":
    url = 'https://www.alkimi.org/how-it-works'  # Replace with the URL you want to scrape
    scrape_images(url)
