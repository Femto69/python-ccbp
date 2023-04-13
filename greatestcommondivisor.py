
m=int(input())
n=int(input())
t=0
s=0
if(m>n):
    s=m
    t=n
else:
    s=n
    t=m
s1=0
for i in range(1,t+1):
    if(m%i==0 and n%i==0):
        s1=i
print(s1)