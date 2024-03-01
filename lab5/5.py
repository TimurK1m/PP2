import re
te=str(input())
tt=r'a.+b\b'
match=re.search(tt,te)
print(match)