n=int(input())
for i in range(1,n+1):
    str1="* "*i
    spaces=" "*(4*(n-i))
    print(str1+spaces+str1)
for i in range(n):
    str2="* "*(n-i)
    spaces2=" "*(4*i)
    print(str2+spaces2+str2)
    