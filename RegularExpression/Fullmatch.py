import re

pattern = '\d{4}-\d{2}-\d{2}' # match a date string in the format yyyy-mm-dd
date_string = ['2023-03-11', '2023-03-111']

'''
Checks if the full string matches the regex pattern
Accepts three parameters: pattern, string to be searched, and optional flags
Returns None if no match was found, returns the match object if a match was found
'''

for i in date_string:
    match = re.fullmatch(pattern, i)

    if match:
        print(f'The date string {i} is valid')
    else:
        print(f'The date string {i} is not valid')