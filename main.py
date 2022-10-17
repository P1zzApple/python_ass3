from flask import Flask, url_for, render_template
from flask import request
from flask_sqlalchemy import *

# Use Moralis ->https://moralis.io/
# in order to get an information about NFT
app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)
'''


@app.route("/")
def home():
    print(url_for('home'))
    return render_template('home.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login logic here"
    return "Rendering Login Form"


with app.test_request_context():
    print(url_for('home'))
    #print(url_for('about', next='/'))
    #print(url_for('static', filename='styles.css'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
