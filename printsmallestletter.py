s=str(input())
min1=0
for i in s:
    uni=ord(i)
    if(i==s[0]):
        min1=uni
    if(uni<min1):
        min1=uni
print(chr(min1))