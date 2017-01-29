# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
# Need to apply for an account first
account_sid = "AC3420982aec0a814507669a0b3ab53d53"
auth_token = "63ddc0ca1d35bbca6a9545ffbd5b7277"
client = TwilioRestClient(account_sid, auth_token)

# Replace this with your own number
my_phone_num = "+8612345678900"
message = client.messages.create(to=my_phone_num, from_="+15034063086",
                                     body="Hello world, I love U!!")
