from slackclient import SlackClient
import time

token = "xoxp-52271374178-52266809857-52436717348-4372e03f1a"
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="")
print sc.api_call(
	"chat.postMessage",channel="#general",text="Hello guys, This is topcoder bot",
	username='topcoder bot',icon_emoji=':robot_face:'
)

if sc.rtm_connect():
	while True:
		print sc.rtm_read()
		time.sleep(1)

	else:
		print "Connection Failed, invalid token?"