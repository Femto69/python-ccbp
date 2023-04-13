n=int(input())
for i in range(1,n+1):
    str1=""
    for j in range(1,n+1):
        str1=". "*(n-j)+"0 "*(2*j-1)+". "*(n-j)
        print(str1)
    break