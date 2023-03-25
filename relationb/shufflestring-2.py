S1=input()
S2=input()
s1=str(S1)
s2=str(S2)
l1=int(len(s1))
s3=""
for i in range(0,l1):
        if(i%2==0):
            s3=s3+s1[i]
        elif(i%2!=0):
            s3=s3+s2[i]
print(s3)