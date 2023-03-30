n=int(input())
for i in range(0,n):
    str1=" "*i +""
    s1=1
    for j in range(0,n-i):
        str1= str1 + str(s1) + " "
        s1=s1+1
    print(str1)