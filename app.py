from flask import Flask
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {'Welcome': 'This is an update to the pipeline.'}


if __name__ == '__main__':
    app.run(debug=True)
