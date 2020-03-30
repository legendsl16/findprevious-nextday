from datetime import datetime,timedelta

while True:
    try:
        enterDate = datetime.strptime(input('Please input a date :'), "%Y-%m-%d")
        print("Today: ", enterDate.strftime("%Y-%m-%d"))
        break
    except ValueError:
        print("You enter INVALID datetime type, *the standar style: YYYY-MM-DD")

n_days = 1
prevDay = enterDate - timedelta(n_days)
nextDay = enterDate + timedelta(n_days)

print("The previous day is: ", prevDay.strftime("%Y-%m-%d"))
print("The next day is: ", nextDay.strftime("%Y-%m-%d"))