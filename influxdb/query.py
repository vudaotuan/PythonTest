__author__ = 'tuanvu'
__create_time__ = '06/05/2015 11:01 AM'

from influxdb.influxdb08 import InfluxDBClient
import time

name = "mc_visit"

json_body = [
    {
        "name": "mc_visit",
        "columns": ["type", "url_base", "user_id"],
        "points": [
            ["add_friend", "friends#show", 23]
        ]
    }
]

client = InfluxDBClient('10.3.9.13', 8989, 'root', 'root', 'mc')
t1 = time.time()

client.write_points(json_body)

rst = client.query("select * from mc_visit limit 100")
print rst

t2 = time.time()

print (t2 - t1)