from datetime import datetime, date

print(datetime.now())
print(date.today())

now = datetime.now()
print(now.strftime("%Y-%m-%d"))
