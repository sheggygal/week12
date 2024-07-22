import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the HTML content
url = "https://github.com/topics"
response = requests.get(url)
print(f"Status Code: {response.status_code}")

# Print the first 100 characters of the HTML content
print(response.text[:100])

# Save the HTML content to a file
with open("webpage.html", "w", encoding="utf-8") as file:
    file.write(response.text)

# Parse the saved HTML content
with open("webpage.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Identify and extract information
titles = [title.text.strip() for title in soup.find_all("p", class_="f3 lh-condensed mb-0 mt-1 Link--primary")]
descriptions = [desc.text.strip() for desc in soup.find_all("p", class_="f5 color-fg-muted mb-0 mt-1")]

# Print the length and content of each extracted list
print(f"Number of titles: {len(titles)}")
print(f"Titles: {titles[:5]}")  # Print the first 5 titles for verification
print(f"Number of descriptions: {len(descriptions)}")
print(f"Descriptions: {descriptions[:5]}")  # Print the first 5 descriptions for verification

# Structure the extracted data into a dictionary
data = {"Title": titles, "Description": descriptions}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df.head())

# Save DataFrame to a CSV file
df.to_csv("github_topics.csv", index=False)