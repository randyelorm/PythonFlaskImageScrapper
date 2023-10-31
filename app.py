
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests_html

app = Flask(__name__)
CORS(app)


# @app.route("/", methods=["POST"])
# def getdata():
#     url = request.form.get("url")
#     webpage = requests.get(url).text
#     soup = BeautifulSoup(webpage, 'html.parser')
#     allurls = []
#     for item in soup.find_all('img', {"src": True}):
#         allurls.append(item['src'])
#     return allurls


# Session stores actions of the user on the page whilst cookie stores it on the computer.
# headers were added so it looks like a request from a browser

@app.route("/", methods=["POST"])
def search():
    search_term = request.form.get("search_term")
    url = f'https://www.google.com/search?q={search_term}&rlz=1C5CHFA_enGH1021GH1021&sxsrf=ALiCzsZxSRkdUWaaI1tweR-MMlOsvqNPHQ:1668530024055&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjjzoXbzrD7AhU3wAIHHZS3B18Q_AUoAnoECAIQBA&biw=1280&bih=913&dpr=2'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    webpage = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage, 'html.parser')
    out_results = []
    for item in soup.find_all('img', {"src": True}):
        out_results.append(item['src'])
    return out_results


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2000)
