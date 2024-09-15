import re

pattern = r'\s+'# match one or more whitespace characters
text = 'The quick brown fox jumps over the lazy dog'

'''
Splits a string at every occurrence of the pattern.
Takes four parameters: pattern, string, optional max number of splits, and optional flags.
Returns a list of the substrings
'''

words = re.split(pattern, text)
print(words)

# Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']