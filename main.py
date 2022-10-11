import os
from urllib.parse import urlparse

import redis

url = urlparse(os.environ.get("REDIS_URL"))
r = redis.Redis(
    host=url.hostname,  # type: ignore
    port=url.port,  # type: ignore
    username=url.username,  # type: ignore
    password=url.password,  # type: ignore
    ssl=True,
    ssl_cert_reqs=None,
)

print("Setting key=value")
r.set("key", "value")
print("Successfull set key=value")
