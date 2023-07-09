n=int(input())
for i in range(0,n):
    if i==0:
        str1="* "+"  "*(2*(n-1))+"*"
    else:
        str1="* "+"  "*(i-1)+"* "+"  "*(2*(n-i-1))+"* "+"  "*(i-1)+"*"
    print(str1)
for i in range(0,n):
    if i==n-1:
        str1="* "+"  "*(2*(n-1))+"*"
    else:
        str1="* "+"  "*(n-i-2)+"* "+"  "*(2*i)+"* "+"  "*(n-i-2)+"*"
    print(str1)