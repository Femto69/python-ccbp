s=str(input())
word=""
for i in s:
    uni=ord(i)
    if(i==" "):
        word=word+" "
        continue
    word=word+chr(uni+1)
print(word)