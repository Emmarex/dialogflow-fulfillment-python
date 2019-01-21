from flask import Flask
from flask import request, redirect, abort

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        return 'Hello, Worl!'
    else:
        abort(404)

# export FLASK_APP=bot_app.py
# export FLASK_ENV=development
# flask run