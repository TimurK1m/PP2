import re 
te=str(input())
tt=r'([A-Z])'
match=re.sub(tt,lambda x:" "+x.group(1).upper(),te)
print(match)