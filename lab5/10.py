import re 

te=str(input())
tt=r'([A-Z])'
match=re.sub(tt,lambda x:"_"+x.group(1).lower(),te)
print(match)