n=int(input())
for i in range(1,n+1):
    str1=" "*(n-i)+""
    if(i==1 or i==2 or i==n):
        for j in range(i):
            str1=str1+"*"+" "
        print(str1)
    else:
        for j in range(i):
            if(j==0 or j==i-1):
                str1=str1+"*"+" "
            else:
                str1=str1+" "+" "
        print(str1)
#The first line has 4 spaces followed by a single star. 
#Each subsequent line has decreasing spaces on either side of the stars until the center line, which contains only stars.