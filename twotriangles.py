n=int(input())
for i in range(0,n):
    if i==0:
        str1="* "+"  "*(2*(n-1))+"*"
    elif i<n-1:
        str1="* "+"  "*(i-1)+"* "+"  "*(2*(n-i-1))+"* "+"  "*(i-1)+"* "
    elif i==n-1:
        str1="* "*2*n
    print(str1)
        