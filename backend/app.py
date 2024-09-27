import os
from flask import Flask
from Controllers.controller import *   
from flask_cors import CORS

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

CORS(app)

@app.route('/', methods=["GET"])
def hello():
    return "Hello World 1"

@app.route('/compare', methods=["POST"])
def compare_image_k():
    return compare()

@app.route('/comparedata', methods=["POST"])
def df_similarity():
    return compare_database()
     
if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")

        
