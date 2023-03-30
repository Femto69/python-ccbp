n=int(input())
s1=0
for i in range(1,n+1):
   for j in range(1,n+1):
      if(i+j==n):
         if(i<j):
            s1=s1+1
print(s1)