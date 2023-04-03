n=int(input())
for i in range(1,2*n+2):
    str1=""
    if i==1 or i==n+1 or i==2*n+1:
        for j in range(0,n):
            str1=str1+"* "
        print(str1)
    elif(i<n):
        for j in range(0,n):
            if(j==0 or j==n-1):
                str1=str1+"* "
            else:
                str1=str1+"  "
        print(str1)
    else:
        for j in range(0,n):
            if j==0 or j==n-1:
                str1=str1+"* "
            else:
                str1=str1+"  "
        print(str1)