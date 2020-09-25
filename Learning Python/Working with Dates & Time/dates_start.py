from datetime import date
from datetime import time
from datetime import datetime

def main():
  # Get todays date
  today = date.today()
  print("Today is", today)
  print("Date componenets:", today.day, today.month, today.year)
  print("Today's weekday # is:", today.weekday())
  days = ["mon", "tue", "wed", "thu", "fri", "sat"]
  print("Which is a:", days[today.weekday()])
  tnow = datetime.now()
  print("The current date and time is ", tnow)

  t=datetime.time(datetime.now())
  print(t)





main()