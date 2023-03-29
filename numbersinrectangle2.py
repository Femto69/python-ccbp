m=int(input())
n=int(input())
s1=1
for i in range(1,m+1):
    str1=""
    for j in range(0,n):
        str1=str1+str(s1)+" "
        s1=s1+1
    print(str1)