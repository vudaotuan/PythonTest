__author__ = 'tuanvu'
__create_time__ = '20/04/2015 8:59 PM'

import requests

url = 'https://graph.facebook.com'

headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0',
}
params = {
    'access_token': 'CAAJY3ZBDkAGwBAHt5NQFZAO5yDeMyDzxmDsr7GLb2ZC7qUKGeGTOZAsttpzd8sHNAtCicsi2aSLPwy3I4HQvdOXscxTmh2kQnZCWriiIY45WdDWL2KpatU8WEAQvTLphee7dQGquZBAj44ZB3SZB4sPFMREb8RJ3Ema7kQtLZBML5q2GIpnBI2rUDUtRUMqC5ASOZAOlzaaztXHTgDFUBTaP7V'}


def info():
    r = requests.get(url + "/v2.3/me", params=params, headers=headers)

    print r.json()


def ad_account_info():
    r = requests.get(url + "/v2.3/me/adaccounts", params=params, headers=headers)

    print r.json()


def create_campain():
    params = {'name': 'My First Campaign',
              'campaign_group_status': 'PAUSED',
              'access_token': 'CAAJY3ZBDkAGwBAHt5NQFZAO5yDeMyDzxmDsr7GLb2ZC7qUKGeGTOZAsttpzd8sHNAtCicsi2aSLPwy3I4HQvdOXscxTmh2kQnZCWriiIY45WdDWL2KpatU8WEAQvTLphee7dQGquZBAj44ZB3SZB4sPFMREb8RJ3Ema7kQtLZBML5q2GIpnBI2rUDUtRUMqC5ASOZAOlzaaztXHTgDFUBTaP7V'}

    r = requests.post(url + "/v2.3/act_213909166/adcampaign_groups", data=params, headers=headers)
    # print r.request

    print r.json()


# 6023502261333
def create_ad_set():
    params = {"name": "My Ad Set",
              "campaign_status": "PAUSED",
              "daily_budget": "10000",
              "bid_type": "CPC",
              "bid_info": "{'CLICKS':150}",
              "targeting": "{'geo_locations': {'countries': ['US']}}",
              "start_time": "1402420337",
              "campaign_group_id": 6023609551333,
              'access_token': 'CAAJY3ZBDkAGwBAHt5NQFZAO5yDeMyDzxmDsr7GLb2ZC7qUKGeGTOZAsttpzd8sHNAtCicsi2aSLPwy3I4HQvdOXscxTmh2kQnZCWriiIY45WdDWL2KpatU8WEAQvTLphee7dQGquZBAj44ZB3SZB4sPFMREb8RJ3Ema7kQtLZBML5q2GIpnBI2rUDUtRUMqC5ASOZAOlzaaztXHTgDFUBTaP7V'}
    r = requests.post(url + "/v2.3/act_213909166/adcampaigns", data=params, headers=headers)

    print r.json()


def create_image():
    params = {"test.jpg": "@E://workspace//PythonTest//facebook//test.jpg",
              'access_token': 'CAAJY3ZBDkAGwBAHt5NQFZAO5yDeMyDzxmDsr7GLb2ZC7qUKGeGTOZAsttpzd8sHNAtCicsi2aSLPwy3I4HQvdOXscxTmh2kQnZCWriiIY45WdDWL2KpatU8WEAQvTLphee7dQGquZBAj44ZB3SZB4sPFMREb8RJ3Ema7kQtLZBML5q2GIpnBI2rUDUtRUMqC5ASOZAOlzaaztXHTgDFUBTaP7V'}
    r = requests.post(url + "/v2.3/act_213909166/adimages", data=params, headers=headers)

    print r.json()

# create_campain()

# 6023609564533
# create_ad_set()

create_image()

# r = requests.get(url + "/v2.3/act_213909166/adcampaigns", params=params, headers=headers)
# print r.json()