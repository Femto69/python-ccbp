s=int(input())
n=int(input())
s1=s
for i in range(1,n+1):
    str1=""
    for j in range(1,i+1):
        str1=str1+str(s1)+" "
        s1=s1+1
    print(str1)