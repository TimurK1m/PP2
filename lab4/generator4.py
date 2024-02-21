def sq(a,b):
    for i in range(a,b+1):
        yield i**2

n=int(input())
z=int(input())
for i in sq(n,z):
    print(i)