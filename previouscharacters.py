s=str(input())
for i in s:
    if(i==" "):
        continue
    uni=ord(i)
    print(chr(uni-1))