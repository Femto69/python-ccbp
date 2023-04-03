n=int(input())
for i in range(1,n+1):
    str1=""
    for j in range(1,n+1):
        str1="0 "*(n-j)+"1 "*(2*j-1)+"0 "*(n-j)
        print(str1)
    break