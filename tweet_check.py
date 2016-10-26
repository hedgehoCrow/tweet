# coding: UTF-8

import tweepy

import key

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print (status.text)
        return True

    def on_error(self, status_code):
        print ('エラー発生: ' + str(status_code))
        return True

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AK, key.AS)

listenr = Listener()
stream = tweepy.Stream(auth, listenr)

stream.sample()     # Twitter全ツイートから1%ピックアップ
#stream.userstream()# ユーザ自信のTL

