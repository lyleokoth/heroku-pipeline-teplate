from flask import Flask
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    x = os.environ['FLASK_ENV'] if os.environ['FLASK_ENV'] else 'Unset'
    return {'Welcome': x}


if __name__ == '__main__':
    app.run(debug=True)