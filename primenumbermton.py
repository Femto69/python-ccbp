M=input()
N=input()
m=int(M)
n=int(N)
s2=""
for i in range(m,n+1):
    s1=0
    if(i==1):
        continue
    for j in range(1,i+1):
        if(i%j==0):
            s1=s1+1
    if(s1<=2):
        s2=s2+str(i)+" "
if(s2==""):
    print("No Prime Numbers Found")
print(s2)