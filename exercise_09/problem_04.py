# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input

import datetime as datetime 


from datetime import date

def days_until_next_birthday(birth_date):
    today = date.today()
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        
    days_until_birthday = (next_birthday - today).days
    return days_until_birthday

def main():
    # Taking birth date input from the user
    while True:
        try:
            birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
            birth_date = date.fromisoformat(birth_date_str)
            break
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
    
    days_until_birthday = days_until_next_birthday(birth_date)
    
    print(f"Days until your next birthday: {days_until_birthday}")

if __name__ == "__main__":
    main()