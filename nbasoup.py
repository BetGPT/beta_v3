import requests
from bs4 import BeautifulSoup
import json

# List of URLs to scrape
urls = [
    "https://cdn.nba.com/news/series-preview-cleveland-cavaliers-4-new-york-knicks-5",
    "https://cdn.nba.com/news/series-preview-sacramento-kings-3-golden-state-warriors-6",
    "https://cdn.nba.com/news/series-preview-phoenix-suns-4-la-clippers-5",
    "https://cdn.nba.com/news/series-preview-memphis-grizzlies-2-los-angeles-lakers-7",
    "https://cdn.nba.com/news/series-preview-boston-celtics-2-atlanta-hawks-7"
]

# Function to scrape data from each URL
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    header_title = soup.find('h1', class_='ArticleHeader_ahTitle__mIo92')
    header_subtitle = soup.find('h1', class_='ArticleHeader_ahSubtitle__4qa5C')
    content = soup.find('div', class_='ArticleContent_article__NBhQ8')

    data = {
        'title': header_title.get_text(strip=True) if header_title else '',
        'subtitle': header_subtitle.get_text(strip=True) if header_subtitle else '',
        'content': [p.get_text(strip=True) for p in content.find_all('p')] if content else []
    }

    return data

# Scrape data from each URL and store in a list
articles = [scrape_data(url) for url in urls]

# Save the scraped data to a JSON file
with open('scraped_data.json', 'w') as json_file:
    json.dump(articles, json_file, indent=2)
