N=input("Enter a number")
n=int(N)
s=str(n)
if(int(s[0])+int(s[1])==7 or s[0]=="7" or s[1]=="7" or n%7==0):
    print("Special Number")
else:
    print("Normal Number")