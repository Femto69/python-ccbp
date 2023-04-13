s=str(input())
str1=""
for i in s:
    uni=ord(i)
    str1=str1+str(uni)+" "
print(str1)
# ord gives the unicode value assigned to the character
# chr gives the character the unicode value is assigned to
# unicode is the value that is assigned to every character
# "abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  for a-z 97-123 and for A-Z 65-91