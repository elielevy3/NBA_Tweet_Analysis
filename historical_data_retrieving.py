import tweepy
import json
from textblob import TextBlob
import nltk
nltk.download('brown')
nltk.download('punkt')

# API keys that yous saved earlier
api_key = "HZjXdUZ5rT8XKcdD9MSFLPBwI"
api_secrets = "IqjvvICp4RJ9Rd8D79BGHk8du4xKO4qeC9nsfMOfTy9f6hSVg6"
access_token = "1540946617955647491-BRvZXiViToEBsKbcnuu8o3OfzmS6XZ"
access_secret = "0BPSkP6kK2RlagSR7Ye349OM1jQycErnEmgFUXdOgpNFL"

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
