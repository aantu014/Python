import calendar

c = calendar.TextCalendar(calendar.SUNDAY)

for m in range(1, 13):
  print(c.formatmonth(2020, m, 0, 0))