def re(N):
    while N!=-1:
        yield N
        N-=1

n=int(input())

for i in re(n):
    print(i)