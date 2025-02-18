from datetime import datetime, timedelta
c_data  =  datetime.now()
n_data = c_data - timedelta(days=5)
print("today is " ,c_data)
print("Date 5 days ago" ,n_data)