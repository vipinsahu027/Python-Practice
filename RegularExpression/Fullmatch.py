import re

pattern = '\d{4}-\d{2}-\d{2}' # match a date string in the format yyyy-mm-dd
date_string = '2023-03-11'

'''
Checks if the full string matches the regex pattern
Accepts three parameters: pattern, string to be searched, and optional flags
Returns None if no match was found, returns the match object if a match was found
'''

match = re. fullmatch(pattern, date_string)

if match:
    print(f'The date string {date_string} is valid')
else:
    print(f'The date string {date_string} is not valid')