import re

pattern = r'\b' # match a word boundary
text = r'The quick \brown fox'

'''
Escape is used to escape special characters so that they can be matched literally.
Accepts one parameter: pattern
Returns the escaped pattern
'''

escaped_pattern = re.escape(pattern)
match = re.search(escaped_pattern, text)

if match:
	print (f'Found a word boundary in the text')
else:
	print(f'Could not find a word boundary in the text')
	

pattern = r'.' # match any char
text = 'The quick brown fox.'

escaped_pattern = re.escape(pattern)
print("new pattern: ", escaped_pattern)
match = re.search(escaped_pattern, text)

if match:
    print(f'Found a dot in the text')
else:
    print(f'Could not find dot in the text')