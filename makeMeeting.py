import jwt
import requests
import json
from time import time
import makeTime

API_KEY = 'UpKzpXeKQ4eIwPe6HPVVeg'
API_SEC = '78mXbnCKXsQk1T6xnzrNI4nLwsZnE7E8v1ME'

def generateToken(expire_in):
    token = jwt.encode(
        {'iss': API_KEY, 'exp': time() + expire_in},
        API_SEC,
        algorithm='HS256'
    )
    return token

meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }

def createMeeting(time_txt , day_txt):
    time_atributes = time_txt.split(':')
    date_atributes = day_txt.split('-')
    hour = int(time_atributes[0])
    minute = int(time_atributes[1])
    month = int(date_atributes[1])
    day = int(date_atributes[0])
    expire_in = makeTime.getValid_Seconds(hour=hour, minute=minute , month=month , day=day) + 2400
    headers = {'authorization': 'Bearer' + generateToken(expire_in=expire_in),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers,
        data=json.dumps(meetingdetails))
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]

    return {
        "meetingUrl" : join_URL,
        "meetingPassword": meetingPassword,
        "valid_time_period_minutes":expire_in/60
    }