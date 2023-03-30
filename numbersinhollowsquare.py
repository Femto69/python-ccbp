n=int(input())
for i in range(0,n):
    str1=""
    if(i==0 or i==n-1):
        for j in range(1,n+1):
            str1=str1+str(j)+" "
        print(str1)
    else:
        for k in range(1,n+1):
            if(k==1 or k==n):
                str1=str1+str(k)+" "
            else:
                str1=str1+" "+" "
        print(str1)