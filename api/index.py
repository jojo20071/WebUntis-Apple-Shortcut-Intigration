from flask import Flask, send_file, jsonify
from flask import request
import webuntis
import datetime
import ast

app = Flask(__name__)

@app.route('/homeoage', methods=['GET'])
def home():
    return("Homepage :)")



if __name__ == '__main__':
    app.run(debug=True)