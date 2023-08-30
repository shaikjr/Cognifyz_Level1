#task 3
#Develop a Python function that validates
#whether a given string is a valid email
#address. Implement checks for the format,
#including the presence of an "@" symbol and
#a domain name

import re

def is_valid_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False


email1 = "user@example.com"
email2 = "invalid.email"
email3 = "another_user@domain"
email4 = "user@.com"
email5 = "@domain.com"

print(f"{email1}: {is_valid_email(email1)}")
print(f"{email2}: {is_valid_email(email2)}")
print(f"{email3}: {is_valid_email(email3)}")
print(f"{email4}: {is_valid_email(email4)}")
print(f"{email5}: {is_valid_email(email5)}")
