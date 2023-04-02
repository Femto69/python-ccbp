n=int(input())
s2=0
for i in range(1,n+1):
    i=int(input())
    s1=0
    for j in range(1,i+1):
        if(i%j==0):
            s1=s1+1
    if(1<s1<=2):
        s2=s2+i
print(s2)