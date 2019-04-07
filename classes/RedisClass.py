import redis
import os


class RedisClass:

    redis_host = os.environ['REDIS_HOST']
    # redis_host = 'localhost'

    def __init__(self):

        self.redis_handle = redis.Redis(host=self.redis_host, port=6379, db=0)

    def set_key(self, key, value):

        status = dict()
        try:
            self.redis_handle.set(key, value)
        except Exception as e:
            status['status'] = 'error'
            status['response'] = str(e)
            return status

        status['status'] = 'success'
        status['response'] = 'value set'
        return status

    def get_key(self, key):

        status = dict()
        ret_val = None
        try:
            ret_val = self.redis_handle.get(key)
        except Exception as e:
            status['status'] = 'error'
            status['response'] = str(e)

        status['status'] = 'success'
        status['response'] = ret_val

        return status























