m=int(input())
n=int(input())
if(m>n):
    s=m
else:
    s=n
r=m*n
for i in range(s,r+1):
    if(i%m==0 and i%n==0):
        print(i)
        break