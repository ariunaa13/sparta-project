import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0',
}

response = requests.get(
    'https://www.greenpeace.org/africa/en/blogs/',
    headers=headers,
)

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.select('body > div.page-template > div > div > ul > li > div')

for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']

    date = article.select_one('span.search-result-item-date').text

    print(f'{date} / {title} / {article_link}')
