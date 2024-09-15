import re

text = "#578491"
pattern = "^#\d{6}$"

'''
Search scans through the provided string looking for the first match.

Accepts three parameters: pattern, string to be searched, and optional flags

Returns None if no match was found, returns the match object if a match was found
'''

match = re.search(pattern, text)

if match:
    print("Match Found")
else:
    print("No match Found")