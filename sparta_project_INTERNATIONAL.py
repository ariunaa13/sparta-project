import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0',}

# international_blog
response = requests.get('https://www.greenpeace.org/international/story/', headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('body > div.page-template > div > div > ul > li > div')
for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('span.search-result-item-date').text
    print(f'{date} / {title} / {article_link}')


# USA_Blog
response = requests.get('https://www.greenpeace.org/usa/stories-victories/', headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('article')
for article in articles:
    a_tag = article.select_one('h3 > a')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('div.teaser-date').text
    print(f'{date} / {title} / {article_link}')


# UK_Blog
response = requests.get('https://www.greenpeace.org.uk/latest-updates/',headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('article')
for article in articles:
    # a_tag = article.select_one('article > header > h3 > a')
    a_tag = article.select_one('header > h3 > a')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('time').text
    print(f'{date} / {title} / "https://www.greenpeace.org.uk{article_link}"')


# AUS_Blog
response = requests.get('https://www.greenpeace.org.au/blog/', headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('article')
for article in articles:
    a_tag = article.select_one('h3 > a')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('div.teaser-date').text
    print(f'{date} / {title} / {article_link}')


#EU_UNIT Blog
response = requests.get('https://www.greenpeace.org/eu-unit/blog/', headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('body > div.page-template > div > div > ul > li > div')
for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('span.search-result-item-date').text
    print(f'{date} / {title} / {article_link}')


#EAST ASIA Blog
response = requests.get('https://www.greenpeace.org/eastasia/blog/', headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('body > div.page-template > div > div > ul > li > div')
for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('span.search-result-item-date').text
    print(f'{date} / {title} / {article_link}')


#Newzealand_Blog
response = requests.get('https://www.greenpeace.org/new-zealand/story/', headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('body > div.page-template > div > div > ul > li > div')
for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('span.search-result-item-date').text
    print(f'{date} / {title} / {article_link}')


#Africa_Blog
response = requests.get('https://www.greenpeace.org/africa/en/blogs/',headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.select('body > div.page-template > div > div > ul > li > div')
for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']
    date = article.select_one('span.search-result-item-date').text
    print(f'{date} / {title} / {article_link}')