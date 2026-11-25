import os, redis
r = redis.from_url(os.environ['REDIS_URL'], decode_responses=True)

token = "9055230595:AAGGQmecsSSruwjRJJs1sKiYGlI9oMqSjqM"
Dev_Blue = token.split(':')[0]
sudo_id = 1920665874
botUsername = ''
from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')
