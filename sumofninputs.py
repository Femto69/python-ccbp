n=int(input())
s=float(input())
s1=0
for i in range(n):
    i=float(input())
    s1=s1+i
    s1=round(s1,3)
if s1==s:
    print("True")
else:
    print("False")