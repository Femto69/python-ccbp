s=int(input())
n=int(input())
w=n
k=0
while(w>=1):
    k=k+w
    w=w-1
x=k+s-1
for i in range(0,n):
    str1=""
    for j in range(0,n-i):
        str1=str1+str(x)+" "
        x=x-1
    print(str1)