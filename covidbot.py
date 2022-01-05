import tweepy

keys = open('keys.txt').read().splitlines()
COMSUMER_KEY    = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY      = keys[2]
ACCESS_SECRET   = keys[3]

auth = tweepy.OAuthHandler(COMSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
