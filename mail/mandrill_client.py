__author__ = 'daotuanvu'
create_date = '2/10/2015'

import mandrill

mandrill_obj = mandrill.Mandrill('pGC4bsXxxFqZraAhwQYJKw')

message = {'from_email': 'pipemarketing@gmail.com',
           'from_name': 'pipemarketing',
           'html': 'Dear *|USER_NAME|*!',
           'subject': 'test merge tags',
           'to': [{'email': 'vu.daotuan@gmail.com', 'type': 'to'}],
           'merge_vars': [{'rcpt': 'vu.daotuan@gmail.com',
                           'vars': [{'content': 'dao tuan vu', 'name': 'USER_NAME'}]}]}
rst = mandrill_obj.messages.send(message=message, async=True)

print rst