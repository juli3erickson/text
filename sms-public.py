from twilio.rest import Client

account_sid = 'A'
auth_token = 'b'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='M',
    body='I can\'t believe this works!',
    to='+1'
)

print(message.sid)