import makeMeeting
from flask import Flask,request, jsonify
#flask cors handing
from flask_cors import CORS , cross_origin

app = Flask(__name__)
#enable cross origin for any ip
CORS(app , resources={r"/":{"origins":"*"}})

#Home Api
@app.route("/")
def main():
    return "hello world"

#First Page
@app.route("/home")
@cross_origin()
def home():
    return "First Page"

@app.route("/schedule_meeting/<time>/<date>")
@cross_origin()
def schedule(time , date):
    return makeMeeting.createMeeting(time_txt=time, day_txt=date)

if __name__ == '__main__':
    app.debug = True
    #init api port and ip address of the server
    app.run(host='localhost',port=5000)
