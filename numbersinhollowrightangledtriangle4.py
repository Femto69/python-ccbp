s=int(input())
n=int(input())
s1=s
for i in range(1,n+1):
    str1=""
    if(i==1 or i==2 or i==n):
        for j in range(0,i):
            str1=str1+str(s1)+" "
            s1=s1+1
        print(str1)
    else:
        for j in range(0,i):
            if(j==0 or j==i-1):
                str1=str1+str(s1)+" "
                s1=s1+1
            else:
                str1=str1+" "+" "
        print(str1)