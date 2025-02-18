from datetime  import datetime,timedelta
t_day = datetime.today()
y_day = t_day - timedelta(days=1)
to_day = t_day + timedelta(days=1)
print("Yesterday:" , y_day)
print("Today: " , t_day)
print("Tomorrow :" , to_day)
