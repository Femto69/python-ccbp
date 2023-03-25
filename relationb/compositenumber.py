N=input()
n=int(N)
s1=0
for i in range(1,n+1):
    if(n%i==0):
        s1=s1+1
if(s1>2):
    print("True")
else:
    print("False")