import re

pattern1 = '\d+' # match one or more digits
pattern2 = '\d+\.\d+' # match one or more digits

text = 'The price of the book is $19.99 and the price of the movie is $12.50'

'''
Searches a string for all non-overlapping matches
Accepts three parameters: pattern, string to be searched, and optional flags
Returns the results of matches
'''

matche1 = re. findall(pattern1, text)
print(f'{text} containns {pattern1}:\n{matche1}')

matche2 = re. findall(pattern2, text)
print(f'{text} containns {pattern2}:\n{matche2}')