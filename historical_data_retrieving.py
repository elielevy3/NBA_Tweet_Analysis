import tweepy
import json
from textblob import TextBlob
import nltk
nltk.download('brown')
nltk.download('punkt')

# API keys that yous saved earlier
api_key = ""
api_secrets = ""
access_token = ""
access_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
api.verify_credentials()

results = api.search_tweets(q="Lebron James", count=500)
# results = json.loads(results["_json"])


for tweet in results["statuses"]:
    text = tweet["text"]
    blob = TextBlob(text)
    # print(blob.noun_phrases)
    print(f"{blob.sentiment}")
# results = [tweet["text"] for tweet in results["statuses"]]
# print(results)
