import os
import json
from twython import Twython
from tips import tips
from random import choice

t = Twython(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'],
      os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

try:
    tweet = t.update_status(status=choice(tips))
    print "Success! Tweet id %s" % tweet.get('id')
except TwythonError as e:
    print e

