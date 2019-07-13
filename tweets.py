#importing library
import tweepy
import json
import pandas as pd
import numpy as np


# Fill the X's with the credentials obtained by above mentioned procedure. 
consumer_key = "XXXXXXXXXX" 
consumer_secret = "XXXXXXXXX"
access_key = "XXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXX"

#twitter handle
username = "enter_username"

# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# Access to user's access key and access secret 
auth.set_access_token(access_key, access_secret) 

# Calling api 
api = tweepy.API(auth) 

#maximum number of tweets to be extracted
number_of_tweets=200
#Using API interface to iterate through username by our own timeline
tweets = api.user_timeline(screen_name=username, count=number_of_tweets) 

#JSONlines of all our tweets from twitter handle 
midas_tweets = [tweet._json for tweet in tweets]

#responses.json to dump all the responses into JSONlines file
with open("responses.json", "w") as write_file:
    json.dump(midas_tweets, write_file)

# open existing data file for manipulation in a dataframe
df = pd.read_json("responses.json")

# list of columns to remove
columns = ['contributors', 'coordinates', 'entities', 'extended_entities', 'favorited', 'geo', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'place', 'possibly_sensitive', 'quoted_status', 'quoted_status_id', 'quoted_status_id_str', 'retweeted', 'retweeted_status', 'source', 'truncated', 'user']

# deleting columns we don't need
df.drop(columns, inplace=True, axis=1)

# number of images present
image_count = []

# now, scan that through every tweet present in the JSONlines.
for tweet in tweets:
  for media in tweet.entities.get("media",[{}]):
    #checks if there is any media-entity
    if media.get("type",None) == "photo":
      # if there is a image add 1
      image_count.append('1')
    else:
      # if there is not a image present then value is None
      image_count.append('None')

new_col = np.asarray(image_count)
df["image_count"] = new_col

df.to_csv('tweets.csv')