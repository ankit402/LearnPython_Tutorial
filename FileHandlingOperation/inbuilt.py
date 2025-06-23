import re

pattern = r'\d+'
test = 'Search the text 123'
match =re.search(pattern, test)
print(match.group())