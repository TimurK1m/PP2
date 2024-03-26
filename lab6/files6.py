import os
g=2
for i in range(97,123):
    file=open(f"lab6\\num6\\{chr(i).upper()}.txt","w+")
    for j in range(1,g):
        file.write(str(j)+" ")
        print(j)
        if j>26:
            break
    g+=1