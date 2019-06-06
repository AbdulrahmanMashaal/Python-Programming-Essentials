"""
Testing template for number of days in a month
"""
###################################################
# Copy and paste your definition of name_to_number() here

import datetime

def days_in_month(year, month):
       
    """
    Inputs:
    year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
    representing the year
    month - an integer between 1 and 12 representing the month
      
    Returns:
    The number of days in the input month.
    """
        
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
    
    
in_year, in_month = (2019, 6)

if datetime.MINYEAR <= in_year and datetime.MAXYEAR >= in_year:
    if in_month>=1 and in_month<=12:
        print(days_in_month(in_year, in_month))
    else:
        print("Error: Please check months part")
else:
    print("Error: please check years part")
     


