t=int(input())
c=0
for i in range(t):
    l=list(map(int,input().split()))
    a=0
    for i in l:
        if i==1:
            a+=1
    if a>=2:
        c=c+1
print(c)