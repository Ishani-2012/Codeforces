n=int(input())
s1=0
s2=0
s3=0
while(n>0):
    a,b,c=map(int,input().split())
    s1+=a
    s2+=b
    s3+=c
    n=n-1
if( s1==0 and s2==0 and s3==0):
    print("YES")
else:
    print("NO")