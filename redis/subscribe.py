#!/usr/bin/env python

# WS server that sends messages at random intervals

import redis,time


redis = redis.Redis(host='127.0.0.1', port=6379, db=0)
sub = redis.pubsub()
sub.subscribe('queue')

for msg in sub.listen():
    # res = sub.get_message()
    print(msg, type(msg))
    if msg['data'] == 1:
        continue
    
    # id = msg['data']
    # if type() == 'bytes':
    sid = msg['data'].decode()

    print('process started ' + sid)
    time.sleep(15)
    redis.set('/status/' + sid, '1', int(time.time()) + 10)
    print('process finished' + sid)


