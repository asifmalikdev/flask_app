# app/redis_app/utils.py
import json
from .redis_client import get_redis

def set_json(key, data, ttl=None):
    value = json.dumps(data)
    client = get_redis()
    if ttl:
        return client.setex(key, ttl, value)
    return client.set(key, value)


def get_json(key):
    value = get_redis().get(key)
    if value is None:
        return None
    return json.loads(value)
