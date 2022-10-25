from flask import Flask, url_for, render_template
from flask import request
from flask_sqlalchemy import *
import api
import requests

# Use Moralis ->https://moralis.io/
# in order to get an information about NFT
app = Flask(__name__)
API_KEY = 'bLWa5EaQFs9umsZIshcBL1zoawIYShqQlMHXdiF7Y7HbxvV7wZvmJIxjibhA1Pcm'
result = api.result
url1 = "https://solana-gateway.moralis.io/nft/mainnet/"
url2 = "/metadata"
#app.config['SQLALCHEMY_DATABASE_URI'] = ''
#db = SQLAlchemy(app)
#db.init_app(app)

'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String)
'''


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
