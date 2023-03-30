n=int(input())
k=int(input())
s=n+(k*(k+1))//2-1
for i in range(1,k+1):
    str1=""
    for j in range(0,i):
        str1=str1+ str(s)+ " "
        s=s-1
    print(str1)