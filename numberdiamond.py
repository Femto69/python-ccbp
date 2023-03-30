n=int(input())
for k in range(1,n):
    str2=" "*(n-k)+""
    s2=1
    for x in range(1,k+1):
        str2=str2+str(s2)+" "
        s2=s2+1
    print(str2)
for i in range(0,n):
    str1=" "*i +""
    s1=1
    for j in range(0,n-i):
        str1= str1 + str(s1) + " "
        s1=s1+1
    print(str1)
#