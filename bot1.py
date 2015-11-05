import tweepy
import psutils
consumer_key = 'WPukxs264EgIdelArs33LLpSd'
consumer_secret = 's7bw8nrIutE07hVIU2oZNerFsaA6Qmj7VznecpB5B72eOWXdYv'
access_token = '14812487-x5hEARyRyVE7X4QQ2X1YhnJbb4bICpRjQgNxNIs8J'
access_token_secret = 'Dozik4wfubV4j8W5zaj8axtsCG4cSzbjm31VveFxqwYfw'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)
twitter.update_status(status="hello world")
cpu_percent = psutils.cpu_pecent(interval =1)
twitter.update_status(status = "CPU percent currently:" + str(cpu_percent))
print("done, exiting")
