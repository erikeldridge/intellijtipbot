import os
import json
from twython import Twython
from features import features
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/auth/start')
def auth_start():
    t = Twython(os.environ['OAUTH_KEY'], os.environ['OAUTH_SECRET'])
    auth = t.get_authentication_tokens(callback_url=os.environ['OAUTH_CALLBACK_URL'])
    response = app.make_response(render_template('auth_start.html', url=auth['auth_url']))
    response.set_cookie('oauth_token_secret',value=auth['oauth_token_secret'])
    return response

@app.route('/auth/complete')
def auth_complete():
    t = Twython(os.environ['OAUTH_KEY'], os.environ['OAUTH_SECRET'],
      request.args.get('oauth_token', ''), request.cookies.get('oauth_token_secret'))
    auth = t.get_authorized_tokens(request.args.get('oauth_verifier', ''))
    return json.dumps(auth)
