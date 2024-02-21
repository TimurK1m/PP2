def evn(N):
    for i in range(0,N+1,2):
        yield i

n=int(input())

b=evn(n)
for i in b:
    print(i,end=',')