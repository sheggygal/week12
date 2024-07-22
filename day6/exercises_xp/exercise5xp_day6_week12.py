import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_current_year_alerts(url):
    # Get the current year
    current_year = datetime.now().year

    # Download the content of the alerts page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all alert entries
        alerts = soup.find_all('h2', class_='node-title')

        # Count alerts from the current year
        current_year_alerts = 0
        for alert in alerts:
            alert_date = alert.find_next_sibling('div', class_='field-item even').get_text(strip=True)
            if str(current_year) in alert_date:
                current_year_alerts += 1

        print(f"Number of security alerts issued by US-CERT in {current_year}: {current_year_alerts}")
    else:
        print(f"Failed to retrieve the page: {response.status_code}")


# URL of the US-CERT alerts page
url = "https://www.us-cert.gov/ncas/alerts"
get_current_year_alerts(url)
