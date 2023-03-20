N=input("Enter a Number")
n=int(N)
if(n%6!=0):
    if(n%3!=0):
        if(n%2!=0):
            print("Number is not divisible by 2, 3 or 6")
        else:
            print("Number is divisible by 2")
    else:
        print("Number is divisible by 3")
else:
    print("Number is divisible by 6")