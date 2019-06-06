"""
Testing template for calculating a persons age in days
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
    
    if datetime.MINYEAR <= year and datetime.MAXYEAR >= year :
        if month>=1 and month<=12:
            date1 = datetime.date(year, month, 1)
            ydate = date1.year
            mdate = date1.month
            date1 = datetime.date(ydate, mdate, 1)
            if mdate < 12:
                date2 = datetime.date(ydate, mdate+1, 1)
            else:
                date2 = datetime.date(ydate+1, 1, 1)
            difference = date2-date1
            #print("days in month function is approved")
            return(difference.days)
        else:
            return(False)
    else:
        return(False)
        
    
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
        date_val = datetime.date(year, month, day)
        #print("is valid date function is approved")
        return(date_val)    
    else:
        return(False)
     
        
def age_in_days(in_year1, in_month1, in_day1):
    
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """    

    if is_valid_date(in_year1, in_month1, in_day1):
        date1_val = (is_valid_date(in_year1, in_month1, in_day1))
    else:
        date1_val = 0
        #print("0")

    if (date1_val !=0):
        todays_date = datetime.date.today()
        if date1_val > todays_date:
            return("0")
        else:
            diff_date = todays_date - date1_val
        return(diff_date.days)
    else:
        return("0")
            
    
    
in_year1, in_month1, in_day1 = (2016, 7, 5)

print(age_in_days(in_year1, in_month1, in_day1))



     


