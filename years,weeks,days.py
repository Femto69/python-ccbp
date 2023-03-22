N=input()
n=int(N)
s1=n//365
s2=(n-(s1*365))//7
s3=(n-(s1*365)-(s2*7))
print(s1)
print(s2)
print(s3)