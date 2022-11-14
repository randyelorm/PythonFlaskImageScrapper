
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def getdata():
    url = request.form.get("url")
    webpage = requests.get(url).text
    soup = BeautifulSoup(webpage, 'html.parser')
    allurls = []
    for item in soup.find_all('img', {"src": True}):
        allurls.append(item['src'])
    return allurls


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2000)
