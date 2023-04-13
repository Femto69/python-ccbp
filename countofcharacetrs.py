s=str(input())
n=int(input())
c=0
for i in s:
    uni=ord(i)
    if(uni==n):
        c=c+1
print(c)