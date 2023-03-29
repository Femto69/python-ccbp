n=int(input())
for i in range(1,n+1):
    s1=1
    str1=""
    for j in range(0,i+1):
        if(s1<=i):
            str1=str1 + str(s1) + " "
            s1=s1+1
        else:
            s1=1
            for k in range(0,i-1):
                str1=str1+ str(s1)+" "
                s1=s1+1
    print(str1)