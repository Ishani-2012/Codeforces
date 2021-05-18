s=input()
a=s[0]
c=1
for i in range(1,len(s)):
    if a==s[i]:
        c+=1
    else:
        a=s[i]
        c=1
    if c==7:
        print("YES")
        break
if c<7:
    print("NO")