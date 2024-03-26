import os 



print("Exist",os.path.exists(r"lab6\num8\sus.txt"))
print("Acces",os.access(r"lab6\num8\sus.txt",os.F_OK))

if os.access(r"lab6\num8\sus.txt",os.F_OK) and os.path.exists(r"lab6\num8\sus.txt"):
    os.remove(r"lab6\num8\sus.txt")
    print("Removed")
else:
    print("Not exist")
    a=open(r"lab6\num8\sus.txt","w")