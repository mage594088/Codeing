import datetime
day = 31
month = 8
year = 2019


x = datetime.datetime(year, month, day)
output = x.strftime("%w")

if output == '1':
    print("Monday")
elif output == '2':
    print("Tuesday")
elif output == '3':
    print("Wednesday")
elif output == '4':
    print("Thursday")
elif output == '5':
    print("Friday")
elif output == '6':
    print("Saturday")
else:
    print("Sunday")
    