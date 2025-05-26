# This files main purpose is to so that I have a place where I can write all 
# the functions related to getting information from the user

from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I" : "Income", "E" : "Expense"}

# Propmt is what we are going to ask the user to input before they give us the date.
# Reason is we can get date from multiple different places and we may be asking 
# date for a different reason
# allow_defult is gonna tell us if we should have the defualt value of today's date. 
# So that they can hjust hit enter and by default it will just select the current date.
# strftime -> String Format Time
# strptime()(string parse time method) is a function used to parse (or read) strings 
# representing dates and times and convert them into datetime objects.

def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    # Now we will try to validate the date from above
    try:
        valid_data = datetime.strptime(date_str, date_format)
        return valid_data.strftime(date_format)
    except ValueError:
        print("Inavlid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount should be a non-negative and a npn-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Inavlid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter Description (optional): ")