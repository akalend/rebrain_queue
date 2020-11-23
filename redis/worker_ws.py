import redis
import time

redis = redis.Redis(host='127.0.0.1', port=6379, db=0)

while 1:
	res = redis.rpop("queue")
	if res is None:
		time.sleep(10)
	else:
		print('process started ' + res.decode())
		time.sleep(15)
		print('process finished' + res.decode())
		# redis.set('status_' + res.decode(), '1', int(time.time()) + 10)	
		res = redis.publish( res.decode(), '1')
		print (res)
		