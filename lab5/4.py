import re
te=str(input())
tt=r'[A-Z]+[a-z]+\b'
match=re.search(tt,te)
print(match)