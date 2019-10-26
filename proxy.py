import requests
from requests_html import HTMLSession

proxy = Blueprint('proxy', __name__)

@proxy.route('/trees', methods=['GET'])
def get_trees():
    session = HTMLSession()
    page = session.get("https://teamtrees.org/")
    elem = page.html.find('#totalTrees', first=True)
    count = elem.attrs['data-count']
    return count