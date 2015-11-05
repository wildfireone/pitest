import tweepy
consumer_key = 'WPukxs264EgldelArs33LLpSd'
consumer_secret = 's7bw8nrlutE07hVIU
access_token
access_token_secret
auth = tweepy.)AuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)
twitter.update("hello world")
print("done, exiting")
