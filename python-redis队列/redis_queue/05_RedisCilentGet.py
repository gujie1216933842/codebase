import RedisQueue

q = RedisQueue('test', 'queue', host="localhost", port=6379, db=1)
q.get()






