import datetime
import time

t = "2006-10-10 15:5:60.00"
q_dt_obj = time.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
new_dt_obj = datetime.datetime.fromtimestamp(time.mktime(q_dt_obj))
print(type(q_dt_obj), q_dt_obj)
print(type(new_dt_obj), new_dt_obj)
