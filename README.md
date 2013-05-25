# Intellij tip bot

The intellij tip bot tweets [intellij](http://www.jetbrains.com/idea/) usage tips.

This bot is not operated by JetBrains.

# Submitting tips

1. Clone the project
2. Add your tip
3. Submit a pull request

- or -

Hit me up on twitter

- or -

Open an issue

# Running your own tip bot

## Set up

1. Clone this repo
1. Set up your environment as described in [Heroku's python set up documentation](https://devcenter.heroku.com/articles/python)

## Authenticate

1. Create an _.env_ file, as described in [Heroku's configuration documentation](https://devcenter.heroku.com/articles/config-vars#local-setup)
1. Create an oauth key/secret pair at dev.twitter.com
1. Populate the _.env_ file as follows:
    OAUTH_KEY=<your app key>
    OAUTH_SECRET=<your app secret>
    OAUTH_CALLBACK_URL=http://localhost:5000/auth/complete
    OAUTH_TOKEN=<populated in the steps below>
    OAUTH_TOKEN_SECRET=<populated in the steps below>
1. Launch the app locally: `$ foreman start`
1. Load http://localhost:5000/auth/start
1. Follow the link and auth with Twitter
1. After you're redirected back to your app, copy/paste the _oauth_token_ and _oauth_token_secret_ into your _.env_ file

## Schedule tweet generator

## License

Copyright 2013 Erik Eldridge

Licensed under the MIT License


