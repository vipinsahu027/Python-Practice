import re

pattern = r'\d+' # match one or more digits
text = 'The price of the book is $19.99 and the price of the movie is $12.50'

'''
Compile a pattern into a regex object.
We can pass the object to other functions.
Makes the code more efficient when we want to reuse a pattern.
'''

regex = re.compile(pattern)
matches = regex.findall(text)

print (matches)