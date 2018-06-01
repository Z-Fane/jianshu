

import redis

try:
    # r = redis.Redis(host='116.62.64.42', port=6379)
    r = redis.Redis(host='127.0.0.1', port=6379)
    r.lpush('jianshu:start_urls', 'https://www.jianshu.com')
    print("压入url成功!")
except Exception as e:
    print("压入失败:{}".format(e))
