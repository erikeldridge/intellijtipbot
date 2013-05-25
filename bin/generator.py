#!/usr/bin/env python

import os
from twython import Twython
from tips import tips
from random import choice

t = Twython(os.environ['OAUTH_KEY'], os.environ['OAUTH_SECRET'],
      os.environ['OAUTH_TOKEN'], os.environ['OAUTH_TOKEN_SECRET'])
print t.update_status(status=choice(tips))
