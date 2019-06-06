"""
Testing template for checking if a date is valid
"""

###################################################
# Copy and paste your definition of name_to_number() here

import datetime

def days_in_month(year, month):
    
    date1 = datetime.date(year, month, 1)
    ydate = date1.year
    mdate = date1.month
    date1 = datetime.date(ydate, mdate, 1)
    if mdate < 12:
        date2 = datetime.date(ydate, mdate+1, 1)
    else:
        date2 = datetime.date(ydate+1, 1, 1)
    difference = date2-date1
    return(difference.days)
    
def is_valid_date(year, month, day):
    
    
    """
    Inputs:
    year  - an integer representing the year
    month - an integer representing the month
    day   - an integer representing the day
      
    Returns:
    True if year-month-day is a valid date and
    False otherwise
    """
    
    if day < days_in_month(year, month) and day >= 1:
        return("True")
    else:
        return("False")
        
    
in_year, in_month, in_day = (2019, 6, 5)

if datetime.MINYEAR <= in_year and datetime.MAXYEAR >= in_year:
    if in_month>=1 and in_month<=12:
        print(is_valid_date(in_year, in_month, in_day))
            
    else:
        print("False")
else:
    print("False")
     


