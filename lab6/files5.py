with open(r"lab6\text.txt","w") as file:
    x=input().split()
    for i in x:
        file.write(i+'\n')
