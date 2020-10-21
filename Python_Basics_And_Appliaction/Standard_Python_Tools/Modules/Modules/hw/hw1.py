from datetime import date, timedelta

current_date = date(*map(int, input().split()))
delta_date = timedelta(days=int(input()))
new_date = current_date + delta_date

print(new_date.year, new_date.month, new_date.day)
