import re
tt=str(input())
match=re.fullmatch(r'a(b{2,3})',tt)
print(match)