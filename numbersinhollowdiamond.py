n=int(input())
for i in range(1,n+1):
    str1=" "*(n-i)+ ""
    s1=1
    if(i==1 or i==2):
        for j in range(1,i+1):
            str1=str1+str(s1)+" "
            s1=s1+1
        print(str1)
    else:
        for j in range(1,i+1):
            if(j==1 or j==i):
                str1=str1+str(s1)+" "
                s1=s1+1
            else:
                str1=str1+" "+" "
                s1=s1+1
        print(str1)
for k in range(1,n):
    str2=" "*k + ""
    s2=1
    if(k==n-2 or k==n-1):
        for l in range(1,n-k+1):
            str2=str2+str(s2)+" "
            s2=s2+1
        print(str2)
    else:
        for l in range(1,n-k+1):
            if(l==1 or l==n-k):
                str2=str2+str(s2)+" "
                s2=s2+1
            else:
                str2=str2+" "+" "
                s2=s2+1
        print(str2)