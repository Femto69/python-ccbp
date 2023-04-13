n=int(input())
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,n+1):
    str1="  "*(n-i)+""
    for j in range(0,i):
        str1=str1+s1[j]+" "
    print(str1)