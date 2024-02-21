import datetime

x=datetime.datetime.now()
print(x)
x=x.replace(microsecond=0)
print(x)