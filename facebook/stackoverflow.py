__author__ = 'tuanvu'
__create_time__ = '15/04/2015 8:50 PM'

# !/usr/bin/python
# coding: utf-8

import facebook
import urllib
import urlparse
import subprocess
import warnings

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID = '660668527411308'
FACEBOOK_APP_SECRET = '519b8a869cf051305e9b4d7d845f80ee'
FACEBOOK_PROFILE_ID = '213909166'


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id=FACEBOOK_APP_ID,
                  client_secret=FACEBOOK_APP_SECRET,
                  grant_type='client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()
