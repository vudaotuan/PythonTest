__author__ = 'Administrator'

import json

data = """{encoding": "UTF-8", "ip": "113.190.157.249", "agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "resolutions": "1920x1080", "user_id": 3752, "title": "K\u1ebft qu\u1ea3 t\u00ecm ki\u1ebfm cho t\u1eeb kh\u00f3a: b\u00e1n m\u00e1y \u1ea3nh | Muare.vn c\u1ed9ng \u0111\u1ed3ng th\u01b0\u01a1ng m\u1ea1i \u0111i\u1ec7n t\u1eed", "item_name": "", "referrer_session": "http://muare.vn/search/36475159/?q=b%C3%A1n+m%C3%A1y+%E1%BA%A3nh+kts&o=relevance", "platform": "Win32", "page_name": "search", "rd_id": "dabe97ac-c712-11e4-bd82-cb58b39a1380", "start_time_visit": 1426489186, "cookie_enabled": 1, "province_name": "ha noi", "referrer_visit": "http://muare.vn/search/36475159/?q=b%C3%A1n+m%C3%A1y+%E1%BA%A3nh+kts&o=relevance", "key_word": "b\u00e1n m\u00e1y \u1ea3nh", "referrer_domain": "muare.vn", "sessionid": 0, "item_id": 0, "province_id": 1, "category_name": "", "lang": "vi", "url": "http://muare.vn/search/36475218/?q=b%C3%A1n+m%C3%A1y+%E1%BA%A3nh&o=relevance", "type": "web", "list_item_id": "", "user_name": "BigMickey", "category_id": 0}"""

print data

data_json = json.loads(data)


print data_json['key_word']

print len(data['enb_list_item'])

for index, item_id in enumerate(data['enb_list_item']):
    print index
    print item_id

a = "None"

if True and a != "None":
    print "a"
else:
    print "b"
