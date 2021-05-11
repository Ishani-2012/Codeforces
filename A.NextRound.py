n,k=map(int,input().split())
l=list(map(int,input().split()))
 
a=l[k-1]
c=0
for i in l:
    if i<1:
        continue
    if i>=a:
        c+=1
print(c)