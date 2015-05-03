# __author__ = 'Administrator'
# email_type = 'text'
# if email_type not in ['text', 'html']:
# email_type = 'html'
# print email_type
#
import datetime

print datetime.datetime.strptime('2015-12-12', '%Y-%m-%d').date()

row = (1, "abc")

sql = """UPDATE email_list_subscribers SET unsubscribed = 1 WHERE listid = ( SELECT list_id FROM custom_campaign WHERE campaign_id = %s ) AND emailaddress = "%s" """ %row

print sql