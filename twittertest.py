import tweepy

import Myauth

# OAuth process, using the keys and tokens

# Creation of the actual interface, using authentication

api1 = tweepy.API(Myauth.auth)
api2 = tweepy.API(Myauth.fake())
# api3 = tweepy.API(Myauth.login())
api = api1
# Sample method, used to update a status
# api.update_status("sad")


def tweetGetir(user_name='ILBERORTAYLIGSU'):
    stuff = api.user_timeline(screen_name=user_name, count=10, include_rts=True, page=4)
    for status in stuff:
        print(status.text, '\n')
    return stuff


#
#
# for f in api.friendships_incoming:
#     print(f.ids)

def makinaSec(id=1):
    if id % 2 == 0:
        api = api1
    else:
        api = api2


def makina(makina_id, page_id, count=20):
    makinaSec(page_id)
    stuff = api.user_timeline(screen_name='ILBERORTAYLIGSU', count=count, page=page_id)
    [print(makina_id, ".makinadan yollandı.", status.text) for status in stuff]


def tweetGetir(username='ILBERORTAYLIGSU', count=200, cpt=20):
    max_page = int(count / cpt) + 1
    c = count
    for i in range(1, max_page):
        makina(i, i, cpt)
        c -= cpt


tweetGetir(count=100, cpt=20)

# makina(1,1,count=10)

#apiNew = tweepy.API(Myauth.login())
