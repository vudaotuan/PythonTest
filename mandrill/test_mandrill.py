__author__ = 'tuanvu'
__create_time__ = '14/05/2015 7:27 PM'


import mandrill

mandrill_client = mandrill.Mandrill('_3TAwqFh9Oy57Y2hfO3OhQ')

print  mandrill_client.users.info()