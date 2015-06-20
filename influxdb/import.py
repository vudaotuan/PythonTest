__author__ = 'tuanvu'
__create_time__ = '05/05/2015 10:17 AM'

from influxdb.influxdb08 import InfluxDBClient
import time

name = "mc_visit"
columns = ["utm_source",
           "utm_medium",
           "utm_campaign",
           "utm_deal",
           "browser_name",
           "browser_version",
           "operating_system",
           "operating_system_version",
           "device_name",
           "resolutions",
           "item_key",
           "item_id",
           "item_name",
           "category_id",
           "category_name",
           "sub_category_id",
           "sub_category_name",
           "source",
           "item_check_sum",
           "url",
           "url_id",
           "site",
           "page_name",
           "key_word",
           "url_check_sum",
           "rd_id",
           "referrer_url",
           "referrer_url_id",
           "referrer_type",
           "referrer_domain",
           "time_day",
           "time_detail",
           "email",
           "province",
           "user_visit_check_sum",
           "sessionid",
           "not_null_search"]

json_body = [
    {
        "name": "mc_visit",
        "columns": ["type", "url_base", "user_id"],
        "points": [
            ["add_friend", "friends#show", 23]
        ]
    }
]

client = InfluxDBClient('10.3.9.13', 8989, 'root', 'root', 'example')
t1 = time.time()

rst = client.query("select * from mc_visit")
print rst

# f = open('visit.csv', 'r')
# for line in f:
#     try:
#         point = line.split(",")
#         client.write_points([{
#                                  "name": name,
#                                  "columns": columns,
#                                  "points": [point]
#                              }])
#         print point
#         time.sleep(0.5)
#         break
#     except:
#         pass

# f.close()

t2 = time.time()


#
# result = client.query('select user_id from user_events;')
#
# print("Result: {0}".format(result))

print (t2 - t1)