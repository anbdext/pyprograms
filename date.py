import datetime
def has_13th_friday(month, year):
    try:
        thirteenth = datetime.date(year, month, 13)
        return thirteenth.weekday() == 4
    except ValueError:
        return False
month = 9
year = 2023
result = has_13th_friday(month, year)
print(f"Does {month}/{year} have a 13th Friday? {result}")

