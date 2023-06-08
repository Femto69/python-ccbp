m=int(input())
n=int(input())
len=n-m+1
s1=0
for i in range(m,n+1):
    s1=s1+i
avg=s1/len
print(s1)
print(avg)
