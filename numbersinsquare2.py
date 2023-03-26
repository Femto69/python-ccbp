N=input()
n=int(N)
for i in range(0,n):
    str1=""
    for j in range(0,n):
        str1=str1+str(n-j)+" "
    print(str1)