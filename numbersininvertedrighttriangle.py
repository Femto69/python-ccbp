N=input()
n=int(N)
for i in range(0,n):
    str1=""
    for j in range(1,n-i+1):
        str1=str1 + str(j)+" "
    print(str1)