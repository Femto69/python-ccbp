n=int(input())
for i in range(1,n+1):
    str1=" "*2*(n-i)+""
    s1=i
    str2=" "*2*(n-i)+""
    s2=i
    if(i==1 or i==2 or i==n):
        for j in range(i):
            str1=str1+str(s1)+" "
            s1=s1-1
        print(str1)
    else:
        for k in range(i):
            if(k==0 or k==(i-1)):
                str2=str2+str(s2)+" "
                s2=s2-1
            else:
                str2=str2+" "+" "
                s2=s2-1
        print(str2)