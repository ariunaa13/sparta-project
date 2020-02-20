import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.greenpeace.org/usa/stories-victories/',headers=headers)
data = requests.get(
    'https://www.greenpeace.org/usa/wp-admin/admin-ajax.php?id=&post_id=0&slug=home&canonical_url=https%3A%2F%2Fwww.greenpeace.org%2Fusa%2Fstories-victories%2F&posts_per_page=10&page=0&offset=0&post_type=stories,%20victories&repeater=default&seo_start_page=1&theme_repeater=teaser-post.php&paging=true&preloaded=false&preloaded_amount=0&order=DESC&orderby=date&action=alm_get_posts&query_type=totalposts'
)

soup = BeautifulSoup(data.text, 'html.parser')

newsgroup = soup.select('article')

for news in newsgroup:
    div1 = newsgroup.select_one('div.textGroup > h3 > a').text
    print(div1)




# for news in newsgroup :
#     title_tag = news.select_one('div > h3 > a')
#     print (title_tag.text)