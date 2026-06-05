# Q1. Write a program to input user's first name & print it's lenght.

var1=input("Enter your first name to know it's length : ")
var2=len(var1)
print("The lenght of your name is : ", var2)

# correct

# Q2. Write  a program to find it's occurrence of '$' in a string.

var1=input("Enter an scentence of your own choice : ")
var2=str.count("$")
print(var2)

# correct

# Q4. Write a program to check if a number entered by the user is odd or even.

var1=int(input("Enter your number: "))
var2=num % 2
if(var2 == 0):
    print("The number given by you is even ! ")
if(var2 != 0):
    print("The number given by you is odd ! ")
 
 # correct   
# Q5. Write a program to find the greatest of 3 numbers entered by the user.

a=int(input("Enter your first number : "))
b=int(input("Enter your second number : "))
c=int(input("Enter your third number : "))
if(a > b and a > c):
    print(a, "is the greatest number amongst all ! ")
elif(b > a and b > c):
    print(b, "is the greatest number amongst all ! ")
elif(c > a and c > b):
    print(c, "is the greatest number amongst all ! ")
elif(a == b and a == c and b == c):
    print("All of the numbers are equal ! ")
    
    # correct
  
# Q5. Write a program to check if a number is a multiple of 7 or not.

var1=int(input("Enter an number : "))
var2=var1%7
if(var2==0):
    print("The number given by you is an multiple of 7 ! ")
elif(var2!=0)
    print("the number given by you is not a multiple of 7 ! " )
    
    #correct