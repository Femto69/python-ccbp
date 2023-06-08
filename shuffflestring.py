s=input()
n=int(len(s))
shuffle=""
for i in range(0,n):
    ind=int(input())
    shuffle=shuffle+s[ind]
print(shuffle)