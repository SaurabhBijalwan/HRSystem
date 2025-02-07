from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/hrsystem'
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == 'password':
        return True
    return False

@app.route('/')
def index():
    return "Welcome to the HR System API"

# Import routes after defining the index route to avoid conflicts
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
