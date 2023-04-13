m=int(input())
n=int(input())
for i in range(m,n+1):
    s1=0
    s2=0
    if(i>0 and i!=1):
        for j in range(1,i+1):
            if(i%j==0):
                s1=s1+1
        if(s1<=2):
            print(i)
            s2=s2+1
            break
if(s2==0):
    print("No prime numbers in the given range")