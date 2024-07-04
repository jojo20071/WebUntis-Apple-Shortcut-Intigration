from flask import Flask, send_file, jsonify
from flask import request
import webuntis
import datetime
import ast

app = Flask(__name__)

@app.route('/homepage', methods=['GET'])
def home():
    return("Homepage :)")

@app.route('/info', methods=['GET'])
def info():
    return("WebUntis-Apple-Shortcut-Intigration Api endpoint to intigrate your WebUntis timetable etc. to your Apple Shortcuts for automations")



if __name__ == '__main__':
    app.run(debug=True)