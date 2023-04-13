n=int(input())
k=int(input())
s1=0
for j in range(1,n+1):
    if(n%j==0):
        s1=s1+1
if(k>s1):
    print(1)
is_condition=k>s1
for i in range(1,n+1):
    if(n%i==0):
        s1=s1-1
        if(s1==k-1):
            print(i)