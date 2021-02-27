import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Isten hozott! Ez egy módosítás!! Version 9"

@app.route('/hogy vagy')
def hello():
    return 'Köszönöm jól, s hogy vagy Te?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
