from flask import Flask
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {'Welcome': 'This is a new branch.'}


if __name__ == '__main__':
    app.run(debug=True)
