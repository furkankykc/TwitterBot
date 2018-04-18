import tweepy

import Myauth


class twitterStream(tweepy.StreamListener):


    def on_status(self, status):
        reply_status = "@%s %s" % (status.author.screen_name, "follow back")
        # api.update_status(status=reply_status, in_reply_to_status_id=status.id)
        api.create_favorite(status)
        api.create_friendship(status.author.screen_name)
        print(status.author.screen_name)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


api = tweepy.API(Myauth.auth)
myStreamListener = twitterStream()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['python'])
