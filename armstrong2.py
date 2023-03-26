N=input()
n=int(N)
for i in range(1,n+1):
    sum_of_power_of_digits=0
    i=str(i)
    power=len(i)
    for j in i:
        j=int(j)
        sum_of_power_of_digits=sum_of_power_of_digits + (j**power)
    
    i=int(i)
    is_armstrong=sum_of_power_of_digits==i
    if is_armstrong:
        print(sum_of_power_of_digits)
    
#This code is designed to check for Armstrong numbers up to a certain limit entered by the user.First, the code reads in a value from the user using the input() function and assigns it to the variable N. Then, the variable n is created by converting N to an integer using the int() function.
# The code then enters a for loop that iterates over each integer from 1 to n (inclusive). For each iteration of the loop, a new variable, sum_of_power_of_digits, is initialized to 0.Next, the integer i is converted to a string using the str() function. The length of this string is stored in the variable power.The code then enters a nested for loop that iterates over each digit in the string i. For each digit, the digit is converted to an integer using the int() function, and then the power of the digit is calculated using the ** operator. This power is then added to the sum_of_power_of_digits variable.
# Once all digits in i have been processed, i is converted back to an integer using the int() function.
# The code then checks if sum_of_power_of_digits is equal to i. If it is, then the number is an Armstrong number, and sum_of_power_of_digits is printed using the print() function.
# Overall, this code checks each integer up to n to see if it is an Armstrong number, which is a number that is equal to the sum of the nth power of its digits. If a number is an Armstrong number, the program prints the number.