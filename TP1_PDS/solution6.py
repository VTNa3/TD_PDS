def is_leap(year):
    """Divisible by 4, except centuries, unless divisible by 400."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year):
    """Return the number of days in a month (1-12), or None if invalid."""
    if month < 1 or month > 12:
        return None
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


print()
for y in [1900, 2000, 2024, 2026]:
    print(y, "leap" if is_leap(y) else "not leap")
print("Feb 2024:", days_in_month(2, 2024), "| Feb 2026:", days_in_month(2, 2026),
    "| Apr:", days_in_month(4, 2026), "| month 13:", days_in_month(13, 2026))

leap_count = 0
for y in range(2000, 2101):
    if is_leap(y):
        leap_count += 1
print("Leap years from 2000 to 2100:", leap_count)