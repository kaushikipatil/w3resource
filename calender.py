"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

def calender_module(yea,mon):
    import calendar
    a=calendar.month(yea,mon)
    return print(a)

print("Enter the month and year in digit")
month=int(input())
year=int(input())

calender_module(year,month)
