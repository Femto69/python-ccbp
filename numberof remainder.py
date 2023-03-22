N=input()
n=int(N)
if((n%5==0 and n%7==0) or n<7):
    print(n)
else:
    print(n%5)
    print(n%7)