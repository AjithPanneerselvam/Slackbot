import os
import time 
import requests
from slackclient import SlackClient 

#BOT_ID = str(os.environ.get("BOT_ID"))
BOT_ID = "<@U1JFV9U49>:"
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(message, channel):
	#data = requests.get('http://api.topcoder.com/v2/data/srm/contests')
	#print data.json()
	
	from urllib2 import Request, urlopen
	request = Request('http://api.topcoder.com/v2/data/srm/contests')
	response_body = urlopen(request).read()
	print response_body
	
	payload = "Done!"
	if BOT_ID.find(message)!= -1:
		slack_client.api_call("chat.postMessage", channel=channel, text=payload, as_user=True)

		
def parse_slack_output(slack_read_content):
	
	READ = slack_read_content
	if READ and len(READ) > 0:
		for read in READ:
			if read and 'text' in read:
				return read['text'], read['channel']

	return None, None


if __name__ == '__main__':

	if slack_client.rtm_connect():
		delay = 1
		print "Bot connected successfully"
		while True:
			message, channel = parse_slack_output(slack_client.rtm_read())
			
			if message and channel:
				handle_command(message, channel)	
			time.sleep(delay)
			
	else:
		print "Couldn't connect, please try again!"	
