from flask import Flask, request, jsonify, render_template
import requests
from requests_html import HTMLSession

app = Flask(__name__, static_url_path='/static')

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
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()