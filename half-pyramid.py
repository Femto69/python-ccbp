n=int(input())
s1=1
for i in range(1,n+1):
    str1=""
    for j in range(0,i):
        str1=str1+str(s1)+" "
        s1=s1+1
    print(str1)