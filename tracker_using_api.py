# newsapi documentation here:
# https://newsapi.org/docs


import requests
import datetime
from pprint import pprint


API_KEY = '' # use your own


def get_news(q, start_date, end_date, language):
    """ return results from newsapi
        free 1,000 requests per day
    """
    global API_KEY
    url = 'https://newsapi.org/v2/everything?q={0}&sortBy=popularity&pageSize=10&from={1}&to={2}&apiKey={3}&language={4}'.format(q, start_date, end_date, API_KEY, language)
    # language = zh or en
    r = requests.get(url)
    return r.json()



def cal_date_interval(days_num):
    today = datetime.datetime.today().date()
    interval = datetime.timedelta(int(days_num))
    start_date = (today - interval).isoformat()
    end_date = today.isoformat()
    return start_date, end_date


if __name__ == '__main__':
    start_date, end_date = cal_date_interval(1)
    pprint(get_news('+长生疫苗', start_date, end_date, 'zh'))
