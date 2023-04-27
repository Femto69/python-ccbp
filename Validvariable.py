s=str(input())
is_true=True
for i in s:
    uni=ord(i)
    is_true=65<=uni<=90 or 97<=uni<=122 or 48<=uni<=57
    if not is_true:
        is_true=False
        break
print(is_true)