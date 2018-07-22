import requests
from bs4 import BeautifulSoup

# use google to find news on some website

EVENT_KEYWORD = '长生疫苗'


def search_google(site_url, keywords):
    url = 'https://www.google.com/search?q=site:{0}%20{1}'.format(site_url, keywords)
    r = requests.get(url)
    return r.content


def main():
    search_result = search_google('yahoo.com', EVENT_KEYWORD)
    print(search_result)


if __name__ == '__main__':
    main()
