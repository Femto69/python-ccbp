N=input()
n=int(N)
s=str(n)
s1=int(s[0])
s2=int(s[1])
s3=int(s[2])
s4=int(s[3])
sum1=s1**4 +s2**4 +s3**4 +s4**4
if(sum1==n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")