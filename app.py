from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import os
import requests
from proxy import proxy

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(proxy)
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

@app.route('/', methods=['GET'])
@auth.login_required
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()