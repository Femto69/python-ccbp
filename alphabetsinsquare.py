n=int(input())
alpha_bets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,n):
    str1=""
    for j in range(0,n):
        str1=str1+alpha_bets[j]+" "
    print(str1)