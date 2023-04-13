n=int(input())
for i in range(0,2*n-1):
    if(i<n):
        str1=" "*(i)+""
        for j in range(0,n-i):
            str1=str1+"* "
    else:
        str1=" "*(2*n-i-2)+""
        for j in range(0,i+2-n):
            str1=str1+"* "
    print(str1)