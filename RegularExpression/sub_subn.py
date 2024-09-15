import re

pattern = r'\b\w{4}\b' # match a word with exactly 4 letters \b is for boundary.
text = 'The quick brown fox jumps over the lazy dog'

'''
Search a string for all non-overlapping occurrences and replace them with a string.
Accepts five parameters: pattern, string to be searched, replacement, optional max number of replacements, and optional flags.
Sub doesn't return anything, subn returns a tuple containing the new string and number of replacements made.
'''

new_text = re.sub(pattern, ' **** ', text)
print(new_text)

# Output: The quick brown fox jumps  ****  the  ****  dog