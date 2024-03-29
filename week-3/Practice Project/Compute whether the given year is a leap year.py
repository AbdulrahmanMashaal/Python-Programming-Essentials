"""
Solution - Compute whether the given year is a leap year.
"""

###################################################
# Is leapyear formula
# Student should enter function on the next lines.
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """	
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


###################################################
# Tests
# Student should not change this code.

year = 2000
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1996
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1800
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 2013
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
