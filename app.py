from flask import Flask, request, jsonify, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


import os
import requests
from requests_html import HTMLSession


app = Flask(__name__, static_url_path='/static')
auth = HTTPBasicAuth()

AUTH_USER = os.environ.get('AUTH_USER')
AUTH_PASS = os.environ.get('AUTH_PASS')

@auth.verify_password
def verify_password(username, password):
    if AUTH_USER and AUTH_PASS:
        return username == AUTH_USER and password == AUTH_PASS
    else:
        return True
    return False

def get_trees_count():
    session = HTMLSession()
    page = session.get("https://teamtrees.org/")
    elem = page.html.find('#totalTrees', first=True)
    count = elem.attrs['data-count']
    return count

@app.route('/trees.json', methods=['GET'])
def trees_proxy():
    return jsonify({'count': get_trees_count()})


@app.route('/', methods=['GET'])
@auth.login_required
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()