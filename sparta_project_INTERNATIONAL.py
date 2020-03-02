# {
#   "type": "service_account",
#   "project_id": "fluid-mote-269912",
#   "private_key_id": "b5ba6e2e439b7636776648aa5d2f66107262c059",
#   "private_key": "",
#   "client_email": "python-client@fluid-mote-269912.iam.gserviceaccount.com",
#   "client_id": "114734346481319964006",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-client%40fluid-mote-269912.iam.gserviceaccount.com"
# }

import requests
from bs4 import BeautifulSoup
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
# from flask import Flask
# # # app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1lTlzEKgDAJmKlRr2rWYvnCNdm3vNa1jXMawxHQVdLxI'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/73.0',
}

response = requests.get(
    'https://www.greenpeace.org/international/story/',
    headers=headers,
)

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.select('body > div.page-template > div > div > ul > li > div')

for article in articles:
    a_tag = article.select_one('a.search-result-item-headline')
    title = a_tag.text
    article_link = a_tag['href']

    date = article.select_one('span.search-result-item-date').text

    # print(f'{date} / {title} / {article_link}')

def main():

    values = [
        ['date', 'title', 'article_link'],
    ]

    body = {
        'values' : values
    }

    credentials = ServiceAccountCredentials.from_json_keyfile_name('fluid-mote-269912-b5ba6e2e439b.json', SCOPES)
    http_auth = credentials.authorize(Http())
    service = build('sheets', 'v4', http=http_auth)

    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                     range = 'Sheet1!A1:B2',
                                                     valueInputOption='RAW',
                                                     body = body
                                                     )

    request.execute()

    if __name__ == '__main__': main()


# if __name__ == '__main__':
#     app.run('0.0.0.0',port=5000,debug=True)