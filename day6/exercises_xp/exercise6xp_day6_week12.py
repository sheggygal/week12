import requests
from bs4 import BeautifulSoup


def fetch_movie_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve the page: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find movie names
    all_h2_tags = soup.find_all('h2')
    movie_names = [h2.get_text(strip=True) for h2 in all_h2_tags[1:]]

    # Find summaries
    summary_divs = soup.find_all('div', class_='article-base rich-content')
    summaries = []
    for div in summary_divs[1:]:
        summary_paragraphs = div.find_all('p')
        summary_texts = [p.get_text(strip=True) for p in summary_paragraphs]
        summaries.append(' '.join(summary_texts))

    return list(zip(movie_names, summaries))


def print_movies(movies, num_movies=10):
    if not movies:
        print("No movies found to select from.")
        return

    for i, (name, summary) in enumerate(movies[:num_movies], 1):
        print(f"Movie {i}:")
        print(f"Name: {name}")
        print(f"Summary: {summary}")
        print()


# URL of the Letterboxd page to scrape
url = "https://letterboxd.com/journal/watchlist-this-july-2024/"

# Fetch movie data
movies = fetch_movie_data(url)

# Print the top 8 random movies
print_movies(movies, num_movies=8)
