import redis


class RedisQueue(object):
    def __init__(self, name, namespace, **kwargs):
        self.__db = redis.StrictRedis(**kwargs)
        self.key = "%s%s" % (namespace, name)

    def qsize(self):
        return self.__db.llen(self.key)

    def empty(self):
        return self.qsize() == 0

    def put(self, item):
        return self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=True):
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)

        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]

        return item

    def get_nowait(self):
        return self.get(False)
