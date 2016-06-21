import os
import time 
import requests
import json
from slackclient import SlackClient 



slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
BOT_ID = str(os.environ.get('BOT_ID'))
RUN_URL = u'http://api.hackerearth.com/code/run/'
CLIENT_SECRET = 'e9b31d9bff43f1a393ec3519515a9cd0b4bc7438'
source = open('hello.py', 'r')


def handle_command(message, channel):
	#print"hey"
	data = {
	    'client_secret': CLIENT_SECRET,
	    'async': 0,
	    'source': source.read(),
	    'lang': "PYTHON",
	    'time_limit': 5,
	    'memory_limit': 262144,
	}
	
	command = message.split()
	command = command[1]
	if BOT_ID in message and "hello.py" in command:

		r = requests.post(RUN_URL, data=data)
		j =  r.json()
		pay = j['run_status']
		pay = json.dumps(pay)
		pay = json.loads(pay)	
		output = "OUTPUT: \n" + pay['output']	
		slack_client.api_call("chat.postMessage", channel=channel, text=output, as_user=True)
		

def parse_slack_output(slack_read_content):
	#print "hello"
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
		print "Error!"	
