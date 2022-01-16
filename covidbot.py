import configparser
import schedule
import json
import requests
import tweepy
<<<<<<< HEAD
import time
from datetime import datetime
=======
>>>>>>> a7aedff0bdf3f4baf280494b9750691b4beeb745

# Getting the keys to the API

KEY_CONFIG_FILE = "keys.cfg"

key_cfg = configparser.ConfigParser()
key_cfg.read(KEY_CONFIG_FILE)

CONSUMER_KEY    = key_cfg.get("KEYS", "CONSUMER_KEY")
CONSUMER_SECRET = key_cfg.get("KEYS", "CONSUMER_SECRET")
ACCESS_KEY      = key_cfg.get("KEYS", "ACCESS_KEY")
ACCESS_SECRET   = key_cfg.get("KEYS", "ACCESS_SECRET")

# Loading in the Twitter Config File

TWITTER_CONFIG_FILE = "twitter.cfg"

twitter_cfg = configparser.ConfigParser()
twitter_cfg.read(TWITTER_CONFIG_FILE)

DEV_RUN = twitter_cfg.getboolean("TWITTER_CONF", "DEV_RUN")
TWEET_POST = twitter_cfg.getboolean("TWITTER_CONF", "TWEET_POST")

# Loading in the Data Config File

DATA_CONFIG_FILE = "data.cfg"
main_cfg = configparser.ConfigParser()
main_cfg.read(DATA_CONFIG_FILE)

# Setting up the API

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

### VARIABLES ###

DATA_URL = 'https://api.corona-zahlen.org/germany'

### FUNCTIONS ###

def get_data():
	req = requests.get(DATA_URL)
	data = json.loads(req.text)
	with open("cov_data.json", "w") as data_saved:
		json.dump(data, data_saved, indent=4, sort_keys=True)

def run():
	if DEV_RUN:
		pass
	get_data()
	tweet = ""
	with open("cov_data.json", "r") as data:
		cov_data = json.load(data)
		tweet = "Infektionen:  " + str(cov_data["cases"]) + "  | + " + str(cov_data["delta"]["cases"])  
		tweet = tweet + "  heute\nTodesfälle:       " + str(cov_data["deaths"]) + "  | + " + str(cov_data["delta"]["deaths"])
		tweet = tweet + "      heute\nInzidenz:          " + str(round(cov_data["weekIncidence"], 2))
		tweet = tweet + "\nR-Wert:                " + str(cov_data["r"]["value"])
		print(tweet)
	if TWEET_POST:
		try:
			api.update_status(tweet)
		except Error as e:
			print('Error occured')
			print(e)

def delete_all_tweets():
    timeline = tweepy.Cursor(api.user_timeline).items()
    for tweet in timeline:
        api.destroy_status(tweet.id)

<<<<<<< HEAD
schedule.every().day.at("17:57").do(run)

while True: 
	schedule.run_pending()
	time.sleep(1)
=======
schedule.every().day.at("06:00").do(run)
while True:
    schedule.run_pending()
    time.sleep(2)
>>>>>>> a7aedff0bdf3f4baf280494b9750691b4beeb745
