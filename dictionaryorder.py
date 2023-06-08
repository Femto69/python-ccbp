s=str(input())
min1=s[0]
max1=s[0]
for i in s:
    uni=ord(i)
    if uni>ord(max1):
        max1=i
    if uni<ord(min1):
        min1=i
str1=min1+" "+max1
print(str1)