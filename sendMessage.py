from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "" 
AUTH_TOKEN = "[AuthToken]" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="", 
	from_="+12019577775", 
	body="hello",  
)
