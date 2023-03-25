M=input()
N=input()
m=int(M)
n=int(N)
for i in range(0,m+2):
    if(i==0 or i==m+1):
        print("+" + "-"*n + "+")
    else:
        print("|" + " "*n + "|")