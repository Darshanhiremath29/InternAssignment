import requests
from bs4 import BeautifulSoup

def scrape_docs(url):
    """
    Fetches and extracts text content from the given URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    return "Error fetching the documentation."

if __name__ == "__main__":
    segment_docs = scrape_docs("https://segment.com/docs/")
    print(segment_docs[:500])  # Print only first 500 characters for preview
