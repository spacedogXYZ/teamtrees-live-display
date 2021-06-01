from flask import Blueprint, jsonify

import requests
from requests_html import HTMLSession

proxy = Blueprint('proxy', __name__)

def get_trees_count():
    session = HTMLSession()
    page = session.get("https://teamtrees.org/")
    elem = page.html.find('#totalTrees', first=True)
    count = elem.attrs['data-count']
    return count

@proxy.route('/trees.json', methods=['GET'])
def trees_proxy():
    return jsonify({'count': get_trees_count()})
