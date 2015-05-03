__author__ = 'tuanvu'
__create_time__ = '18/04/2015 1:46 AM'

from facebookads.session import FacebookSession
from facebookads.api import FacebookAdsApi
from facebookads.objects import AdGroup


my_app_id = '660668527411308'
my_app_secret = '519b8a869cf051305e9b4d7d845f80ee'
my_access_token = 'CAACEdEose0cBAPOgi9SLi3GbdDdqEkPLOv5TPrtyz1jLhPVLPZBpINyxfSW3aVZA66AdSYRv9LkLTjQdOZB7UcqJQZBr8oTKVha2gE9Cpw1FSZCRvNc2GTwGsPWT9AmkFOOe3YjSGZBBI8vh2aTeY4QkYFX6ZAtkZAhAHPEuwVEPgI6h4u6C5oiQSrH559tlqwfsmfhxLooXY7idn041xVJZC'
my_session = FacebookSession(my_app_id, my_app_secret, my_access_token)
my_api = FacebookAdsApi(my_session)
FacebookAdsApi.set_default_api(my_api)

new_adgroup = AdGroup(parent_id='act_213909166')
new_adgroup[AdGroup.Field.name] = 'My Adgroup'
new_adgroup[AdGroup.Field.campaign_id] = <AD_SET_ID>
new_adgroup[AdGroup.Field.creative] = {
    'creative_id': <CREATIVE_ID>
}
new_adgroup.remote_create()