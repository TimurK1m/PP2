import re 

te=str(input())
tt=r'_([a-z])'
match=re.sub(tt,lambda x: x.group(1).upper(),te)
print(match)