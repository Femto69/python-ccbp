s=int(input())
n=int(input())
s1=s
for i in range(0,n):
    str1=" "*(i*2)+""
    if(i==0 or i==n-2 or i==n-1):
        for j in range(0,n-i):
            str1=str1+str(s1)+" "
            s1=s1+1
        print(str1)
    else:
        for j in range(0,n-i):
            if(j==0 or j==n-i-1):
                str1=str1+str(s1)+  " "
                s1=s1+1
            else:
                str1=str1+" "+" "
        print(str1)