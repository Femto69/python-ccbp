m=int(input())
n=int(input())
str1=""
s2=0
for i in range(m,n+1):
    i=str(i)
    l=len(i)
    s1=0
    for j in range(l):
        s1=s1+int(i[j])**l
    if(s1==int(i)):
        str1=str1+str(i)+" "
        s2=s2+1
if(s2==0):
    print("-1")
print(str1)