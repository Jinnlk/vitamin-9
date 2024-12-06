from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "Keep pushing forward.",
    "Believe in yourself.",
    "You can achieve anything!",
    "Hard work beats talent when talent doesn’t work hard."
]

@app.route('/quote', methods=['GET'])
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)
