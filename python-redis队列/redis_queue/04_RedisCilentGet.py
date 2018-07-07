import RedisQueue
import time

q = RedisQueue.RedisQueue('test', 'queue', host="localhost", port=6379, db=1)
while 1:
    result = q.get_nowait()
    if not result:
        break
    print("output.py: data {} out of queue {}".format(result, time.strftime("%c")))
    time.sleep(2)



