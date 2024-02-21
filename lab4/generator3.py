def txh(N):
    for i in range(0,N+1):
        if i%3==0 and i%4==0:
            yield i 

n=int(input())

b=txh(n)

for i in b:
    print(i)