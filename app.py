from flask import Flask, request, jsonify
# from flask-sqlalchemy import SQLAlchemy
# from flask-marshmallow import Marshmallow
import os

# init appp
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///' + \
    os.path.join(basedir, 'db.sqlite')


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/json', methods=['GET'])
def json():
    return jsonify({"get": 'get'})


if __name__ == "__main__":
    app.run(debug=True)
