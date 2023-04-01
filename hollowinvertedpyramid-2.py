n=int(input())
for i in range(0,n):
    str1=""
    if(i==0 or i==n-2 or i==n-1):
        for j in range(1,n-i+1):
            str1=str1+str(j)+" "
        print(str1)
    else:
        for j in range(1,n-i+1):
            if(j==1 or j==n-i):
                str1=str1+str(j)+" "
            else:
                str1=str1+" "+" "
        print(str1)
# The code uses two nested loops to generate the pattern. The outer loop iterates over the line numbers, 
# while the inner loop generates the numbers and spaces for each line.

#In the if-else statement inside the outer loop, the code checks if the current line is the first, second to last, or last line. 
# If it is, it generates a line with consecutive numbers from 1 to n. Otherwise, it generates a line with numbers only at the beginning and end,
#  and spaces in between. 
