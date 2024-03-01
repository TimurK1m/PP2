import re
tt=str(input())
match=re.search(r'\b[a-z]+(_[a-z]+)+\b',tt)
print (match)