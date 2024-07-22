import requests

# URL for the robots.txt file
url = "https://en.wikipedia.org/robots.txt"

# Download the content of the robots.txt file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the robots.txt file
    print(response.text)
else:
    print(f"Failed to retrieve robots.txt: {response.status_code}")
