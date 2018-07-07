import RedisQueue

import time

q = RedisQueue.RedisQueue('test', 'queue', host="localhost", port=6379, db=1)
for i in range(5):
    q.put(i)
    print("input.py: data {} enqueue {}".format(i, time.strftime("%c")))
    time.sleep(1)
