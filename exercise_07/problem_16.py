# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number
import re

def is_valid_email(email):
    if len(email) > 256:
        return False


    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    match = re.match(pattern, email)
    
    if match:
        at_index = email.find('@')
        last_period_index = email.rfind('.')
        
        if at_index > 0 and (last_period_index - at_index) > 1 and (len(email) - last_period_index) > 1:
            return True
        
    return False


print(is_valid_email("example@example.com"))
print(is_valid_email("ex@ample@domain.com"))
print(is_valid_email("example@domain.c")) 
print(is_valid_email("example.domain.com"))
print(is_valid_email("example@domaincom"))
print(is_valid_email("1example@domain.com"))
print(is_valid_email(".example@domain.com"))
print(is_valid_email("example@domain..com"))
