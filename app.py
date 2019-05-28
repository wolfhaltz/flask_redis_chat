import datetime
import redis
from flask import (
    Flask,
    Response,
    redirect,
    render_template,
    request,
    session,
)

app = Flask(__name__)
app.secret_key = 'asdf'

# redis, port, db, charset to decode everything:
r = redis.StrictRedis('redis', 6379, 0, charset='utf-8', decode_responses=True)

if __name__ == '__main__':
app.run()