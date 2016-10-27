# coding: UTF-8

import sys
import tweepy

import key
import loop_destroy

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print ('ツイート') # 量が多すぎるのでサンプルでは関数の判定のみ
        #print (status.text)
        return True

    def on_error(self, status_code):
        print ('エラー発生: ' + str(status_code))
        return True

    def on_connect(self):
        print ('接続しました')
    
    def on_disconnect(self, notice): 
        print ('接続されました:' + str(notice.code))
        
    def on_limit(self, track):
        print ('受信リミットが発生しました:' + str(track))

    def on_timeout(self):
        print ('タイムアウト')

    def on_warning(self, notice):
        print ('警告メッセージ:' + str(notice.message))

    def on_exception(self, exception):
        print ('例外エラー:' + str(exception))
        
auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AK, key.AS)

while True:
    try:
        listenr = Listener()
        stream = tweepy.Stream(auth, listenr)
        stream.sample()     # Twitter全ツイートから1%ピックアップ
        #stream.userstream()# ユーザ自信のTL
    except:
        sys.exit(0)

