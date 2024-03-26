import os

dir=os.listdir()
for i in dir:
    print(os.path.isdir(i))
    print(os.path.isfile(i))
    print("----")