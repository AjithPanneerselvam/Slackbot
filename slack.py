import os
import time 
from slackclient import SlackClient 

BOT_ID = os.environ.get("BOT_ID")

#constants
AT_BOT = "<@" + BOT_ID + ">:"
COMMAND = "<@" + BOT_ID + ">:"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
	print "&&&&&& this is handle func"
	print command
	payload = "Done!"
	if "<@U1JFV9U49>:" in command:
		slack_client.api_call("chat.postMessage", channel=channel, text=payload, as_user=True)

		
def parse_slack_output(slack_rtm_output):
	
	print "....../////...../////// the read output is ...///...."
	print slack_rtm_output
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
		for output in output_list:
			if output and 'text' in output:
				print ".\n\n************ the channel is *****  " + output['channel']
				print output['text']
				return output['text'], output['channel']

	return None, None



if __name__ == '__main__':

	READ_WEBSOCKET_DELAY = 1

	if slack_client.rtm_connect():
		print "StarBot connected and running!"
		
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			
			if command and channel:
				handle_command(command, channel)	
			time.sleep(READ_WEBSOCKET_DELAY)
			
	else:
		print "Connection failed. Invalid Slack token or bot ID?"	
