m=int(input())
n=int(input())
k=m*n
s1=k
for i in range(0,m):
    str1=""
    for j in range(0,n):
        str1=str1+str(s1)+" "
        s1=s1-1
    print(str1)