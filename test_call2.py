from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd5f8c7c48f9d99295a43c96b9f10c623"
# Your Auth Token from twilio.com/console
auth_token  = "f6944916f27ab8c85689a618d9121e44"

client = Client(account_sid, auth_token)
call = client.calls.create(
    to="+79992115175", 
    from_="+12692485119",
    url="voice.xml"
)


print(call.sid)


