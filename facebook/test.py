__author__ = 'tuanvu'
__create_time__ = '14/04/2015 8:55 PM'

from facebookads.api import FacebookAdsApi
from facebookads.objects import AdUser
from facebookads.objects import AdAccount
from facebookads.objects import AdCreative
from facebookads.objects import AdGroup

import requests

def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with

    # print file.text
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

my_app_id = '660668527411308'
my_app_secret = '519b8a869cf051305e9b4d7d845f80ee'
# my_access_token = 'CAAJY3ZBDkAGwBALbBZA4MzREehUucvo2iZAP3kM1ivwIAyj6iX1ktjaOrUog88XgKv1mPmuZC4ZBOFxwehVjnH776IXGJpGLpozbL3X3xPRZAh7nwZCK3J2cTk7zrFfA8EgoyioOxuITX1HAo7qDxKlRoZB5nk0ZAbJYSOI34K12zFLZCojyQRWAWi5cWza7NEUi0kb6pPrzgK9gupW9t7BGCX'
my_access_token = '660668527411308|3wEipQaqi6UT8A-i30N5nH9GC_8'
# my_access_token = get_fb_token(my_app_id, my_app_secret)
print my_access_token

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = AdUser(fbid='me')
accounts = me.get_ad_accounts()

# Output account ID
for account in accounts:
    print account[AdAccount.Field.id]


# from facebookads.objects import AdImage
#
# image = AdImage(parent_id='act_213909166')
# image[AdImage.Field.filename] = 'E:/workspace/PythonTest/facebook/test.jpg'
# image.remote_create()
#
# # Output image hash.
# print image[image.Field.hash]

# 3228b064a41d2270f78ba4469807a748
# Then, create an ad creative by referencing the image hash returned in the previous call
# creative = AdCreative(parent_id='act_213909166')
# creative[AdCreative.Field.name] = 'sample creative'
# creative[AdCreative.Field.title] = 'hello world'
# creative[AdCreative.Field.body] = 'I\'m an ad'
# creative[AdCreative.Field.object_url] = 'www.newmail.goku.me'
# creative[AdCreative.Field.image_hash] = '3228b064a41d2270f78ba4469807a748'
# creative.remote_create()
# creative_id = creative.get_id_assured()
#
# print creative_id
# creative_id=6023620186533
# # Finally, create your ad by referencing the ad creative.
# adgroup = AdGroup(parent_id='act_213909166')
# adgroup[AdGroup.Field.name] = 'My Ad'
# adgroup[AdGroup.Field.campaign_id] = 6023609564533
# adgroup[AdGroup.Field.creative] = {'creative_id': str(creative_id) }
# adgroup[AdGroup.Field.status] = AdGroup.Status.paused
# adgroup.remote_create()