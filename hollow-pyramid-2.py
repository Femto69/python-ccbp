n=int(input())
for i in range(1,n+1):
    str1=" "*(n-i)+""
    s1=1
    if(i==1 or i==2 or i==n):
        for j in range(i):
            str1=str1+str(s1)+" "
            s1=s1+1
        print(str1)
    else:
        for j in range(i):
            if(j==0 or j==i-1):
                str1=str1+str(s1)+" "
                s1=s1+1
            else:
                str1=str1+" "+" "
                s1=s1+1
        print(str1)
#The first line has 4 spaces followed by a single 1. 
# Each subsequent line has decreasing spaces on either side of the numbers until the center line,
#  which contains consecutive numbers from 1 to n.