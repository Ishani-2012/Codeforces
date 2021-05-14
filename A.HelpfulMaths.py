s=input()
l=[]
for i in s:
    l=[i for i in s if i.isdigit()]
l.sort()
for i in range(len(l)-1):
    print(l[i],"+",sep="",end="")
print(l[len(l)-1])