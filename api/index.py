from flask import Flask, send_file, jsonify,send_from_directory, abort
from flask import request
import webuntis
import datetime
import ast
import os

app = Flask(__name__)

DOWNLOAD_DIRECTORY = "uploads"

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
@app.route('/time/1', methods=['GET'])
def time1():
    error = ""
    result = ""
    ggg = []
    if len(s.my_timetable(start=(today + datetime.timedelta(days=-3)),end=(today + datetime.timedelta(days=-3)))) != 0:
        for ooo in ast.literal_eval(str(s.my_timetable(start=(today + datetime.timedelta(days=1)),end=(today + datetime.timedelta(days=1))))):
            if "code" not in ooo:
                ggg.append(int(ooo.get("startTime",0)))


    if len(ggg) != 0:
        if len(str(min(ggg))) == 3:
            result = str(min(ggg))[0]+":"+str(min(ggg))[1]+str(min(ggg))[2]
        else:
            result = str(min(ggg))[0]+str(min(ggg))[1]+":"+str(min(ggg))[2]+str(min(ggg))[3]

    else:
        error = 12

    data = {
        "result": result,
        "error" : error

    }
    return (jsonify(data))


#------------------------------------------------------------
@app.route('/download', methods=['GET'])
def download():
    file_path = os.path.join('uploads', "Wann Beginnt Schule Morgen.shortcut")
    return send_from_directory('uploads', "Wann Beginnt Schule Morgen.shortcut", as_attachment=True)

@app.route('/homepage', methods=['GET'])
def home():
    return("Homepage :)")

@app.route('/info', methods=['GET'])
def info():
    return("WebUntis-Apple-Shortcut-Intigration Api endpoint to intigrate your WebUntis timetable etc. to your Apple Shortcuts for automations")



if __name__ == '__main__':
    app.run(debug=True)