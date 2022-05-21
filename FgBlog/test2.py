import datetime
date = datetime.date.today()
print(str(datetime.date.today()).replace('-', '')[6:8])
print(int(str(datetime.date.today()).replace('-', '')[6:8]) > 4)