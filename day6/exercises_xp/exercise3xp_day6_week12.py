import requests
from bs4 import BeautifulSoup

# URL for the Wikipedia Main Page
url = "https://en.wikipedia.org/wiki/Main_Page"

# Download the content of the main page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all header tags (h1, h2, h3, h4, h5, h6)
    headers = []
    for i in range(1, 7):
        headers.extend(soup.find_all(f'h{i}'))

    # Display the headers
    print("Header Tags from Wikipedia's Main Page:")
    for header in headers:
        print(f"{header.name}: {header.get_text(strip=True)}")
else:
    print(f"Failed to retrieve the Wikipedia Main Page: {response.status_code}")
