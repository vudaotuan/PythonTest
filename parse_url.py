__author__ = 'tuanvu'
__create_time__ = '19/04/2015 6:45 PM'

url = 'http://muachung.vn/do-dung-gia-dinh/goi-cao-su-non-mem-mai-co-lon-86380.html?_sc=mc&_tp' \
      '=re&_zn=hot&utm_deal=86380'

import urlparse


def get_advertisement_information(url, type):
    par = urlparse.parse_qs(urlparse.urlparse(url).query)
    if type in par:
        return par[type][0]
    else:
        return "NONE"


def get_advertisement_source_fields(data):
    # advertisement_source_dimension
    utm_source = get_advertisement_information(data['url'], "utm_source")
    utm_medium = get_advertisement_information(data['url'], "utm_medium")
    utm_campaign = get_advertisement_information(data['url'], "utm_campaign")
    utm_deal = get_advertisement_information(data['url'], "utm_deal")

    if '?' in utm_medium:
        utm_medium = utm_medium[:utm_medium.index('?')]
    if '?' in utm_campaign:
        utm_campaign = utm_campaign[:utm_campaign.index('?')]

    if '?' in utm_deal:
        utm_deal = utm_deal[:utm_deal.index('?')]
    if '?' in utm_deal:
        utm_deal = utm_deal[:utm_deal.index('?')]

    if utm_source == 'NONE' and utm_medium == 'NONE' and utm_campaign == 'NONE':
        utm_source = get_advertisement_information(data['url'], "_sc")
        utm_medium = get_advertisement_information(data['url'], "_tp")
        utm_campaign = get_advertisement_information(data['url'], "_zn")
        utm_deal = get_advertisement_information(data['url'], "_deal")

        if '?' in utm_medium:
            utm_medium = utm_medium[:utm_medium.index('?')]
        if '?' in utm_campaign:
            utm_campaign = utm_campaign[:utm_campaign.index('?')]

        if '?' in utm_deal:
            utm_deal = utm_deal[:utm_deal.index('?')]
        if '?' in utm_deal:
            utm_deal = utm_deal[:utm_deal.index('?')]

    return [utm_source, utm_medium, utm_campaign, utm_deal]

def get_advertisement_information_with_two_type(url, type1, type2):
    par = urlparse.parse_qs(urlparse.urlparse(url).query)
    if type1 in par:
        return par[type1][0]
    elif type2 in par:
        return par[type2][0]
    else:
        return "NONE"

data = dict()
data['url'] = url

# print get_advertisement_source_fields(data)
print get_advertisement_information_with_two_type(url, "utm_source", "_sc")