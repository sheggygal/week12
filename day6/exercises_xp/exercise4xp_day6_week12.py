import requests
from bs4 import BeautifulSoup


def check_title(url):
    # Download the content of the page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if the page contains a title tag
        title_tag = soup.title

        if title_tag:
            print(f"Title found: {title_tag.string}")
        else:
            print("No title tag found on the page.")
    else:
        print(f"Failed to retrieve the page: {response.status_code}")


# URL to check
url = input("Please, enter the url: ")
check_title(url)