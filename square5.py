s=int(input())
n=int(input())
for i in range(0,n):
    s1=s
    str1=""
    for j in range(0,n):
        str1=str1+str(s1+j)+" "
    print(str1)