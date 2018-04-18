import tweepy

import fileOp

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)




def login():
    print(auth.get_authorization_url())
    verifier = input('Verifier:').strip()
    acc = auth.get_access_token(verifier)
    print(acc)
    auth.set_access_token(acc[0], acc[1])

    # self.auth = tweepy.OAuthHandler(acc[0], acc[1])
    # self.auth.set_access_token(acc[0], acc[1])
    fileOp.writeFile(auth.get_username(), str(acc[0]), str(acc[1]))
    return auth

