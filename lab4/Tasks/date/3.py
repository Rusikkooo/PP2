from datetime import datetime,timedelta
now = datetime.now()
clean_time = now.replace(microsecond=0)
print(clean_time)