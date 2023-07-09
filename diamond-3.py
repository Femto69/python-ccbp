n=int(input())
for i in range(0,n):
    str1=""
    ls=". "*(n-i-1)
    ch="0 "*(2*i+1)
    rs=". "*(n-i-1)
    str1=ls + ch  + rs
    print(str1)
for i in range(1,n):
    str1=""
    ls=". "*i
    ch="0 "*(2*(n-i)-1)
    rs=". "*(i)
    str1=ls+ch+rs
    print(str1)