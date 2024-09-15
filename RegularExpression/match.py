import re

pattern = 'The' # match the word "The" at the beginning of a string
text = 'The quick brown fox'

'''
Checks if the beginning of the string matches the pattern
Accepts three parameters: pattern, string to be searched, and optional flags
Returns None if no match was found, returns the match object if a match was found
'''

match = re.match(pattern, text)

if match:
    print(f'The text string starts with the word "{pattern}"')
else:
    print(f'The text string does not start with the word "{pattern}"')