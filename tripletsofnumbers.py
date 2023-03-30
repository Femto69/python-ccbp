n=int(input())
s1=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if(i+j+k==n):
                if(i<j<k):
                    s1=s1+1
print(s1)