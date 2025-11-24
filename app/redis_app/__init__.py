import redis

class FlaskRedis:
    def __init__(self):
        self.client = None

    def init_app(self, app):
        redis_url = app.config.get("REDIS_URL", "redis://localhost:6379/0")

        self.client = redis.from_url(
            redis_url,
            decode_responses=True
        )

        app.extensions["redis_client"] = self.client

    def get_client(self):
        return self.client


redis_app = FlaskRedis()
redis_client = redis_app  
