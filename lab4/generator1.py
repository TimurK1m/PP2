def sq(N):
    for i in range(1,N+1):
        yield i**2

a=int(input())
b=sq(a)
for i in b:
    print(i)