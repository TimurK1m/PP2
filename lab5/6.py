import re 
te =str(input())
tt=r'[ ,.]'
match=re.sub(tt,':',te)
print(match)