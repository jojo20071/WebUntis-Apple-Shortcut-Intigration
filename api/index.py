from flask import Flask, send_file, jsonify
from flask import request
import webuntis
import datetime
import ast

app = Flask(__name__)



today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

s = webuntis.Session(
    server='https://herakles.webuntis.com',
    username='haede5044',
    password='Jojo1809!',
    school='Erich-Kästner-Gym',
    useragent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36'
)

s.login()


#------------------------------------------------------------
@app.route('/timetable', methods=['GET'])
def tt():
    return str(s.my_timetable(start=(today),end=(today)))


@app.route('/homepage', methods=['GET'])
def home():
    return("Homepage :)")

@app.route('/info', methods=['GET'])
def info():
    return("WebUntis-Apple-Shortcut-Intigration Api endpoint to intigrate your WebUntis timetable etc. to your Apple Shortcuts for automations")



if __name__ == '__main__':
    app.run(debug=True)