N=input()
n=int(N)
s1=0
for i in range(0,3):
    q=n//10
    r=n%10
    s1=s1+r**3
    n=q
    continue
print(s1)
if(int(s1)==n):
    print("True")
else:
    print("False")