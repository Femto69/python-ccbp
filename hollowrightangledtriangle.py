n=int(input())
for i in range(0,n):
    if i==0:
        str1="+ "*n
    elif i<n-1:
        str1="  "*i+"*"+" "*(2*(n-i-1)-1)+"*"
    elif i==n-1:
        str1="  "*i+"*"
    print(str1)