M=input()
N=input()
m=int(M)
n=int(N)
for i in range(0,m):
    if(i%2==0):
        print("+ "*n)
    elif(i%2!=0):
        print("- "*n)