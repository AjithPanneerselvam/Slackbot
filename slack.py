import os
import time 
import requests
import json
from slackclient import SlackClient 


slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
BOT_ID = str(os.environ.get('BOT_ID'))
RUN_URL = u'http://api.hackerearth.com/code/run/'
CLIENT_SECRET = 'e9b31d9bff43f1a393ec3519515a9cd0b4bc7438'


def handle_command(message, channel):
	
	if BOT_ID in message:
		command = message.split()
		file_name= str(command[1])
		directory = os.getcwd() + '/' + file_name 
		is_present = os.path.isfile(directory)

		if is_present:
			source = open(file_name, 'r')
			data = {
	   		 'client_secret': CLIENT_SECRET,
	   		 'async': 0,
   	 		'source': source.read(),
	   	 	'lang': "PYTHON",
	   	 	'time_limit': 5,
    			'memory_limit': 262144,
			}
			
			r = requests.post(RUN_URL, data=data)
			j =  r.json()
			pay = j['run_status']
			pay = json.dumps(pay)
			pay = json.loads(pay)	
			output = "OUTPUT: \n" + pay['output']	
			slack_client.api_call("chat.postMessage", channel=channel, text=output, as_user=True)
		
		else:
			output = "File is not present in current working directory!"
			slack_client.api_call("chat.postMessage", channel=channel, text=output, as_user=True)
		

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
		print "Error!"	
