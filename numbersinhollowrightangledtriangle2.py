n=int(input())
s1=1
for i in range(0,n):
    str1=""
    if(i==0 or i==n-2 or i==n-1):
        for j in range(1,n-i+1):
            str1=str1+str(s1)+" "
            s1=s1+1
        print(str1)
    else:
        for j in range(1,n-i+1):
            if(j==1 or j==n-i):
                str1=str1+str(s1)+" "
                s1=s1+1
            else:
                str1=str1+" "+" "
                s1=s1+1
        print(str1)