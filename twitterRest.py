import time

import googletrans
import tweepy
from requests.exceptions import Timeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError

import Myauth

tweepy.RateLimitError

class TwitterClient(object):

    def __init__(self, auth=None):
        # Attempt authentication
        try:
            if (auth != None):
                self.auth = auth
                self.api = tweepy.API(self.auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)
                print("Login was successful for ", self.auth.get_username())
            else:
                self.auth = Myauth.login()

            self.tweet_count_max = 300  # To prevent Rate Limiting #max twit sayisi
        except:
            print("Error: Authentication Failed")

    # def login(self):
    #     print(self.auth.get_authorization_url())
    #     verifier = input('Verifier:').strip()
    #     acc = self.auth.get_access_token(verifier)
    #     print(acc)
    #     #self.auth = tweepy.OAuthHandler(acc[0], acc[1])
    #     #self.auth.set_access_token(acc[0], acc[1])
    #     #fileOp.writeFile(self.auth.get_username(), str(acc[0]), str(acc[1]))
    #     return acc

    def followByHashtag(self, hashtag):
        for tweet in tweepy.Cursor(self.api.search, q=hashtag).items():
            self.api.create_friendship(screen_name=tweet.author.screen_name)
            print(tweet.author.screen_name)

    # def getUsername(self):
    #     return self.api.auth.get_username()

    def followFollowersFollowing(self, who, followCount=1000):
        for follower in tweepy.Cursor(self.api.followers, who).items():
            try:
                if (follower.followers_count > followCount):
                    self.api.create_friendship(screen_name=follower.screen_name)
                    print(follower.screen_name)
                time.sleep(2)
            except ReadTimeoutError:
                print("ReadTimeoutError")
            except ConnectionError:
                print("ConnectionError")
            except Timeout:
                print("timeoutError")

        self.followFollowersFollowing(tweepy.Cursor(self.api.friends, who).items()[23], followCount)

    def removeNotFriends(self):
        followers = self.api.followers_ids()
        friends = self.api.friends_ids()
        for f in friends:
            if f not in followers:
                print("Unfollow {0}?".format(self.api.get_user(f).screen_name))
                if input("Y/N?") == 'y' or 'Y':
                    self.api.destroy_friendship(f)

    def getUserTweetCount(self, who):
        return (self.api.get_user(screen_name=who).statuses_count)

    def getProfile(self, who):
        # print(who.screen_name)
        print(self.api.get_user(screen_name=who).statuses_count)
        self.printTweets(
            self.api.user_timeline(screen_name=who, count=self.api.get_user(screen_name=who).statuses_count))

    def getTweetsFrom(self, who, page=0, count=20):
        print(who)
        try:
            if (page == 0):
                return self.api.user_timeline(screen_name=who, count=20)
            else:
                return self.api.user_timeline(screen_name=who, count=count, page=page)
        except tweepy.TweepError:
            return
    def tweetSomeThing(self, text):
        self.api.update_status(text + "\n TweetBot kodlama denemeleri tafafindan tweetlendi.")
        print("Twitledin : " + text)

    def retweet(self, tweet):
        self.api.retweet(tweet.id)
        print("rtledin " + tweet.text)

    def retweetFromHashtag(self, hashtag, favCount):
        for tweet in tweepy.Cursor(self.api.search, q=hashtag).items():
            print(tweet.text + " " + str(tweet.favorite_count))
            if tweet.favorite_count > favCount:
                self.retweet(tweet)

    def replyAHashtag(self, hashtag, text, favCount):
        for tweet in tweepy.Cursor(self.api.search, q=hashtag).items():
            print(tweet.text + " " + str(tweet.favorite_count))
            if tweet.favorite_count > favCount:
                self.api.update_status(status=text, in_reply_to_status_id=tweet.id)

    def retweetFromUser(self, who, favCount=10):
        for tweet in self.getTweetsFrom(who):
            # if tweet.retweet_count>rt:
            if tweet.favorite_count > favCount:
                self.retweet(tweet)
                print(tweet)

    def favUsersTweet(self, who):
        for tweet in self.getTweetsFrom(who):
            # if tweet.retweet_count>rt:
            self.api.create_favorite(tweet)
            print("begendin : " + tweet)

    def stealTweetfrom(self, who, favCount):
        for tweets in self.getTweetsFrom(who):
            if tweets.favorite_count > favCount:
                try:
                    self.tweetSomeThing(tweets.text)
                except:
                    print("duplicate")
                print(tweets)

    def stealTweetfromtr(self, who, favCount):
        translate = googletrans.Translator()
        for tweets in self.getTweetsFrom(who):
            if tweets.favorite_count > favCount:
                try:
                    self.tweetSomeThing(translate.translate(tweets.text, dest='tr').text)
                    print(translate.translate(tweets.text, dest='tr'))
                except:
                    print("duplicate")
                print(tweets)

    def sendDM(self, who, message):
        self.api.send_direct_message(screen_name=who, text=message)

    def deleteAllTweets(self):
        for status in tweepy.Cursor(self.api.user_timeline).items():
            self.api.destroy_status(status.id)

    def confirmAllRequests(self):
        for f in self.api.friendships_incoming:
            print(f.ids)

    def printTweets(self, tweets):
        print(len(tweets))
        [print(u.text) for u in tweets]
    def getTextList(self,tweet):
        arr = []
        for t in tweet:
            arr.append(t.text)
            #print(t.text)
        return arr

    def getRateLimit(self):
        return \
        self.api.rate_limit_status()['resources']['business_experience']['/business_experience/dashboard_features'][
            'remaining']
    #
    # def canIread(self):
    #     return if(self.api.rate_limit_status()!=0)
