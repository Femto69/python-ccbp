s=input()
str1=""
l=int(len(s))
for i in range(0,l):
    if s[i-1]==" " or i==0:
        uni=ord(s[i])
        str1=str1+chr(uni+1)
    else:
        str1=str1+s[i]
print(str1)