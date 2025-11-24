# app/redis_app/redis_client.py
from flask import current_app

def get_redis():
    return current_app.extensions["redis_client"]


def set_value(key, value, ttl=None):
    client = get_redis()
    if ttl:
        return client.setex(key, ttl, value)
    return client.set(key, value)


def get_value(key):
    return get_redis().get(key)


def delete_value(key):
    return get_redis().delete(key)


def exists(key):
    return get_redis().exists(key)


def increment(key):
    return get_redis().incr(key)
