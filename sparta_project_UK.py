import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0',
}

response = requests.get(
    'https://www.greenpeace.org.uk/latest-updates/',
    headers=headers,
)

soup = BeautifulSoup(response.text, 'html.parser')

# articles = soup.select('#main > div.main-section')
articles = soup.select('article')

for article in articles:
    # a_tag = article.select_one('article > header > h3 > a')
    a_tag = article.select_one('header > h3 > a')
    title = a_tag.text
    article_link = a_tag['href']

    date = article.select_one('time').text

    print(f'{date} / {title} / "https://www.greenpeace.org.uk{article_link}"')
