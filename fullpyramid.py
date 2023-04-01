n=int(input())
for i in range(1,n+1):
    str1=" "*(n-i)+""
    s1=1
    for j in range(i):
        str1=str1+str(s1)+" "
        s1=s1+1
    print(str1)