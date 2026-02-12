import re

def validate_date():
    date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    
    user_date = input("Enter a date (DD/MM/YYYY): ")
    
    if re.match(date_pattern, user_date):
        print("Valid date format!")
    else:
        print("Wrong Date Format")

validate_date()
