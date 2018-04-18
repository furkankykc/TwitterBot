# TwitterBot

## First of all you must create an instance with your Token from twitterrest.py TwitterClient class
```
twitter = TwitterClient(auth=Myauth.login())
```
## Now you can use functions in TwitterClient class
###### For example:
```
tweets = twitter.getTweetsFrom('example_twitter_username')
```
###### With printTweets with printTweets function
```
twitter.printTweets(tweets)
```

## Function list:
###### followByHashtag
follow users by hashtag statuses, you can set minimum favori count 
###### followFollowersFollowing
 follow some users followers 
###### removeNotFriends
 unfollow not following you back 
###### getProfile
 for get somebodys full tweets 
###### getTweetsFrom
 for getting somebodys tweet with page and count parametters
###### tweetSomeThing
 tweet some text you want
###### retweet
 retweet some tweet with tweet id
###### retweetFromHashtag
 retweet tweets in somehastag with parametter fav or retweet count 
###### replyAHashtag
 comment per tweet in a hashtag
###### retweetFromUser
 retweet all tweets in a user's timeline 
###### favUsersTweet
  favorite all tweets in a user's timeline 
###### stealTweetfrom
  steal all tweets in a user's timeline with parametter retweet count or favorite count 
###### stealTweetfromtr
  stealing tweets with translate language 
###### sendDM
  sending Direct Messages 
###### deleteAllTweets
  delet all of your tweets 
###### confirmAllRequests
  confirm all of your follow request if your account is private 
###### printTweets
  for printing tweets 
###### getTextList
  get your tweet's text in a list 
###### getRateLimit
  return your remaining request  

