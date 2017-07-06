import time
from twython import Twython
from twython import TwythonStreamer

# Getting Twitter API ready
twitter = Twython(TAPIKEY, TAPIKEYSECRET, oauth_version=2)
ACCESSTOKEN = twitter.obtain_access_token()
twitter = Twython(TAPIKEY, access_token=ACCESSTOKEN)


#print(twitter.get_user_timeline(screen_name=''))


class TDataStream(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			txt = str(data['text'].encode('utf-8'))
			print(txt)

	def on_error(self, status_code, data):
		print(status_code)
		self.disconnect()


streamer = TDataStream(TAPIKEY, TAPIKEYSECRET, TACCESSTOKEN, TACCESSTOKENSECRET)

while True:
	keyword = input()
	if keyword is not None:
		streamer.statuses.filter(track=keyword)
		time.sleep(1)
