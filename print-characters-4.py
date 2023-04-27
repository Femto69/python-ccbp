s=str(input())
m=int(input())
n=int(input())
word=""
for i in s:
    if(m>n):
        if(n<=ord(i)<=m):
            word=word+i+" "
    else:
        if(m<=ord(i)<=n):
            word=word+i+" "
print(word)