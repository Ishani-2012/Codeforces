s=input()
s=s.lower()
for i in s:
    if (i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and i!='y'):
        print("."+i,end="")