from flask import Flask, url_for, render_template
from flask import request
import api
import requests


app = Flask(__name__)
result = [api.result]
url1 = "https://solana-gateway.moralis.io/nft/mainnet/"
url2 = "/metadata"


@app.route("/")
def home():
    print(url_for('home'))
    return render_template('home.html', title='NFT Aggregator')


@app.route("/result", methods=["POST", "GET"])
def result():
    headers = {
        "accept": "application/json",
        "X-API-Key": "bLWa5EaQFs9umsZIshcBL1zoawIYShqQlMHXdiF7Y7HbxvV7wZvmJIxjibhA1Pcm"
    }
    if request.method == 'POST':
        address = request.form['Type']
        url = url1 + address + url2
        response = requests.get(url, headers=headers)

    result = response.text
    return render_template('result.html', title='NFT', menu=result)


with app.test_request_context():
    print(url_for('home'))
    #print(url_for('about', next='/'))
    #print(url_for('static', filename='styles.css'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
