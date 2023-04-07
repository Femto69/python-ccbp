n=int(input())
k=int(input())
s1=0
s2=0
for i in range(1,n+1):
    if(n%i==0):
        s1=s1+1
s3=s1+1-k
for j in range(1,n+1):
    s2=s2+1
    if(n%j==0):
        if(s2==s3):
            print(j)