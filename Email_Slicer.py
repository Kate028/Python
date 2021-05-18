# Ask user to enter email address
from sqlite3 import SQLITE_CREATE_TEMP_TRIGGER


email = input('Enter your email address: ').strip()

# Slice and store username
username = email[:email.index('@')]

# slice and store domain name
domain = email[email.index('@') +1:]

# Make output result using username and domain name
result = "your username = {}\n Your domain = {} ".format(username,domain)

# Print the result
print(result) 

Calender
Email Slicer
Hangman
Number Guessing
