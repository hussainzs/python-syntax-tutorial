from datetime import datetime

name = "Alice"
age = 30
height = 5.6

info = f"Name: {name}, Age: {age}, Height: {height:.1f}, Debug: {age=}, Uppercase: {name.upper()!r}"
# Output: Name: Alice, Age: 30, Height: 5.6, Debug: age=30, Uppercase: 'ALICE'
print(info)

print(f"Debug: {name=}")
# Output: Debug: name='Alice'

today = datetime(year=2017, month=1, day=27)
print(f"Today is {today}")
# Output: Today is 2017-01-27 00:00:00
print(f"{today = :%A, %B %d, %Y}")
# Output: today = Friday, January 27, 2017
'''
%A: Full weekday name (e.g., "Friday")
%B: Full month name (e.g., "January")
%d: Day of the month as a zero-padded decimal number (e.g., "27")
%Y: Year with century as a decimal number (e.g., "2017")
'''

name = "Fred"
print(f"He said his name is {name!r}.")
# Output: He said his name is 'Fred'.