n=int(input())
k=0
s=n
while(s>=1):
    k=k+s
    s=s-1
for i in range(0,n):
    str1= " "*2*i+""
    for j in range(0,n-i):
        str1=str1+str(k)+" "
        k=k-1
    print(str1)