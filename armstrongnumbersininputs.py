n=int(input())
for i in range(0,n):
    i=int(input())
    i=str(i)
    l=int(len(i))
    s1=0
    for j in range(0,l):
        s1=s1+int(i[j])**l
    if(s1==int(i)):
        print(s1)