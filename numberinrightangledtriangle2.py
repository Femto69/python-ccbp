N=input()
n=int(N)
for i in range(1,n+1):
    str1=""
    spaces="  "*(n-i)
    for j in range(1,i+1):
        str1=str(j)+" "+str1
        
    str1=spaces+str1
    print(str1)