#!/usr/bin/env python
# -*- coding: utf-8 -*-

##argfile = str(sys.argv[1])
import Myauth
import fileOp
from twitterRest import TwitterClient

argfile = '/home/furkankykc/Desktop/twBot.txt'
fileOp.readFile()

apiTw = TwitterClient(auth=Myauth.fake())

#[print(u.text) for u in apiTw.getTweetsFrom('furkankykc')]
apiTw.stealTweetfromtr('CRDBBankPlc',5)