import redis

r = redis.Redis(host='47.97.165.75', port=6379, password=123)  # host后的IP是需要连接的ip，本地是127.0.0.1或者localhost
r.set('name', 'test')
print(r.get('name'))
