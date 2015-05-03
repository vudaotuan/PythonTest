__author__ = 'tuanvu'
__create_time__ = '01/05/2015 2:23 PM'


import requests

def get_fb_token(app_id, app_secret):
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/v2.3/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with

    print file.url
    print file.text

    # print file.text
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

print get_fb_token('660668527411308', '519b8a869cf051305e9b4d7d845f80ee')