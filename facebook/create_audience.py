__author__ = 'tuanvu'
__create_time__ = '23/04/2015 7:17 PM'


# create audience
from facebookads.objects import CustomAudience

audience = CustomAudience(parent_id=account_id)

audience[CustomAudience.Field.name] = 'My new CA'
audience[CustomAudience.Field.description] = 'People who visited my website'

audience.remote_create()


# add email to audience
from facebookads.objects import CustomAudience

audience = CustomAudience('<AUDIENCE_ID>')
users = ['test1@example.com', 'test2@example.com', 'test3@example.com']

audience.add_users(CustomAudience.Schema.email_hash, users)


# update audience name
from facebookads.objects import CustomAudience

audience = CustomAudience('<AUDIENCE_ID>')
audience[CustomAudience.Field.name] = 'Updated name for CA'
audience.remote_update()


# remove user from audience
from facebookads.objects import CustomAudience

audience = CustomAudience('<AUDIENCE_ID>')
users = ['test1@example.com', 'test2@example.com', 'test3@example.com']

audience.remove_users(CustomAudience.Schema.email_hash, users)


# To edit Opt-out link
from facebookads.objects import CustomAudience

audience = CustomAudience('<AUDIENCE_ID>')
audience[CustomAudience.Field.opt_out_link] = 'http://www.yourdomain.com/optout'
audience.remote_update()