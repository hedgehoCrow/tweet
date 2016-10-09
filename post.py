# coding: UTF-8

import key
from twitter import Twitter, OAuth

t = Twitter(auth = OAuth(key.CK, key.CS, key.AK, key.AS))

text = 'test'
statusUpdate = t.statuses.update(status=text)

# 生の投稿データの出力
print (statusUpdate)

# 要素を絞った投稿データの出力
print (statusUpdate['user']['screen_name'])
print (statusUpdate['user']['name'])
print (statusUpdate['text'])

