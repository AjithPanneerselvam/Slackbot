import os
from flask import Flask, request, Response
from slackclient import SlackClient
#from twilio import twiml
#from twilio.rest import TwilioRestClient

SLACK_WEBHOOK_SECRET = os.environ.get('xoxp-52271374178-52266809857-52436717348-4372e03f1a', None)
print SLACK_WEBHOOK_SECRET

app = Flask(__name__)
slackclient = SlackClient(os.environ.get('xoxp-52271374178-52266809857-52436717348-4372e03f1a',None))

@app.route('/slack',methods=['POST'])
def slack_post():
	if request.form['token'] == SLACK_WEBHOOK_SECRET:
		channel = request.form['#general']
		username = request.form['ajith']
		payload = {"text":"Hey there!!"}
	return Response(), 200

@app.route('/', methods = ['GET'])
def test():
	return Response('It works!')

if __name__ == '__main__':
	app.run(debug=True)