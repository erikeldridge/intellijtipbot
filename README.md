# Intellij tip bot

The [IntelliJ tip bot](https://twitter.com/intellijtipbot) tweets [IntelliJ](http://www.jetbrains.com/idea/) usage tips.

**Note:** Many of these tips are specific to a keymap, e.g., _Mac OS X_, which may or may not be the one you use. I use the _Vim_ and _Mac OS X 10.5+_ keymaps, for example. If a given tip doesn't work with your settings, use the description to find the equivalent.

Special thanks to [@moh](https://twitter.com/moh) (and contributors) for making his [IntelliJ shortcuts list](https://github.com/almalkawi/wiki/wiki/IntelliJ-IDEA-shortcuts) available.

# Submitting tips

1. Clone the project
2. Add your tip
3. Submit a pull request

\- or -

Hit [me](http://twitter.com/erikeldridge) up on twitter

\- or -

Open an issue

# Maintaining and repurposing tip bot

## Set up

1. Clone this repo
1. Set up Heroku, as described in the [Heroku quickstart](https://devcenter.heroku.com/articles/quickstart)
1. Create a Heroku app
1. Set up your environment, as described in [Heroku's python set up documentation](https://devcenter.heroku.com/articles/python)

## Authenticate

1. Create an application at [dev.twitter.com](https://dev.twitter.com)
1. Click the "create OAuth access token"
1. Create an _.env_ file, as described in [Heroku's configuration documentation](https://devcenter.heroku.com/articles/config-vars#local-setup)
1. Populate the _.env_ file as follows:

        CONSUMER_KEY=<your app's consumer key>
        CONSUMER_SECRET=<your app's consumer secret>
        ACCESS_TOKEN=<your app's access token>
        ACCESS_TOKEN_SECRET=<your app's access token secret>

## Add tips

1. Modify _tips.py_ to include your content
1. Commit your changes and push them to your Heroku app

## Test locally

1. Export _.env_ vars: `for v in $(cat .env); do export $v; done`
1. Generate tweet: `$ python bin/generator.py`

## Test remotely

1. Push your _.env_ settings to heroku: `$ heroku config:set $(cat .env)`
1. Generate tweet: `$ heroku run python bin/generator.py`

**Note:** duplicate tweets will be blocked, as described by Twitter's status/update API docs:
> For each update attempt, the update text is compared with the authenticating user's recent tweets. Any attempt that would result in duplication will be blocked, resulting in a 403 error.

## Schedule

1. Add the [Scheduler add-on](https://devcenter.heroku.com/articles/scheduler) to your app
1. Configure Scheduler to run `python bin/generator.py` at your desired rate

# License

Copyright 2013 Erik Eldridge and others

Licensed under the MIT License


