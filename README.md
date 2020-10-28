# Dev Blog Server

## About

This is a repo built using Flask, GraphQL (ariadne) and MongoDB, intending to build a metadata backend for my personal blog (https://www.blog.viniciusarre.dev).

This metadata would include comment data (with threads and responses), as well as workers for notifying the users of new comments or responses to their comments.

## Running it

You can run it by creating the venv folder inside this repo's folder by running

`virtualenv venv`

Then, activate the virtual environment by running

`source venv/bin/activate`

Then install the dependencies on `requirements.txt` by running:

`pip install -r requirements.txt`

Finally, you can run the app by running:

`python index.py`

Done. You should be able to run it now. 