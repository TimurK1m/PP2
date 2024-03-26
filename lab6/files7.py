file1=open(r"lab6\num7\a")
file2=open(r"lab6\num7\b")
with open(r"lab6\num7\a","r") as l:
    with open(r"lab6\num7\b","w") as i:
        i.write(l.read())