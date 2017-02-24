from twilio.rest import TwilioRestClient
import time

# Your twilio account information
account_sid = "INSERT YOUR ACCTSID"
auth_token = "INSERT YOUR TOKEN"

# The number you want to send to, and your registered twilio number
to_number = "+1111111111"
from_number = "+1111111111"

# The text that will be sent
text = "CUSTOM TEXT MESSAGE HERE"

# The hour that you want the text sent
time_hour = 9

hasSent = False

def send_sms():
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=to_number, from_=from_number, body=text)

while(1):
    current_time = time.localtime()
    hour = current_time.tm_hour
    if(hour == time_hour and not hasSent):
        send_sms();
        hasSent = True
    if(hour == time_hour + 1):
        hasSent = False
    time.sleep(10)
