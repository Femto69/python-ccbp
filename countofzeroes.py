n=int(input())
s=str(n)
s1=0
for i in s:
    if i=="0":
        s1=s1+1
if s1>3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")