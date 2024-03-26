x=str(input())
big=0
lil=0
for i in range(0,len(x)):
    if x[i] == x[i].upper() and x[i]!=" ":
        big+=1
    elif x[i]==x[i].lower() and x[i]!=" ":
        lil+=1
print(big,lil)