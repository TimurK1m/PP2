import re
tt=str(input())
match=re.fullmatch(r'a(b*)',tt)
print(match)
