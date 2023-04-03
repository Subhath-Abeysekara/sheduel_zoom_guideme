import time
import datetime

def getExpireTime(hour , minute , month , day):
    current_time = datetime.datetime.now()
    time_tuple = (current_time.year, month, day, hour, minute, 0, 0, 0, 0)
    seconds = time.mktime(time_tuple)
    return seconds

def getValid_Seconds(hour , minute , month , day):
    expire_time = getExpireTime(hour=hour , minute=minute, month=month , day=day)
    now_time = time.time()
    valid_seconds = expire_time - now_time
    return valid_seconds