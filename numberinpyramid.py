N=input()
n=int(N)
M=input()
m=int(M)
for i in range(1,m+1):
    str1=""
    k=m-i
    spaces=" "*k
    for j in range(n,i+n):
        str1= str1+  str(j)+" "
        
    str1=spaces+str1
    print(str1)