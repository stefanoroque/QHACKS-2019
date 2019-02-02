import tweepy
import time
#insert your Twitter keys here
consumer_key ='LBmiVSC1no4EnykqxKfFZJ4em'
consumer_secret='J3klllRhlzz7NmkkMGOdFt2xpMCwSzv1D6WVWsFbqcXP0DmKjc'
access_token='334992084-6DctgZkCdNjvdcMjBzFBUxdPW2iFbKxq6alGHvNt'
access_token_secret='4SQz5BlvYbk7abAABlmWWDnNubC1LIM8b5W2p5yFl0GQR'
twitter_handle='realJDAnthony'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

list= open('twitter_followers.txt','w')

if(api.verify_credentials):
    print ('We successfully logged in')

user = tweepy.Cursor(api.followers, screen_name=twitter_handle).items()
#for user in tweepy.Cursor(api.followers, screen_name=twitter_handle).items():
while True:
	try:
		u = next(user)
		list.write(u.screen_name +' \n')
		print (u.screen_name)
	except tweepy.RateLimitError:
		#logging.info("[%s] Timeout Reached, Sleep for 15 minutes before restart" % self.process_name)
		print ('We got a timeout ... Sleeping for 15 minutes')
		time.sleep(15*60)
	except StopIteration:
		break

# while True:
#     try:
#         u = next(user)
#         list.write(u.screen_name +' \n')

#     except:
#         time.sleep(15*60)
#         print ('We got a timeout ... Sleeping for 15 minutes')
#         u = next(user)
#         list.write(u.screen_name +' \n')

# list.close()