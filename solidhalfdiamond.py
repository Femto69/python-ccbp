n=int(input())
for i in range(1,2*n+1):
    str1=""
    if(i<=n):
        for j in range(1,i+1):
            str1=str1+"*"+" "
        print(str1)
    else:
        for j in range(1,2*n-i+1):
            str1=str1+"*"+ " "
        print(str1)