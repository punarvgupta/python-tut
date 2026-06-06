# Q1.the program to enter names of their 3 favorite movies and store them in a list .

'''
var1=input("Enter the name of your first favorite movie : ")
var2=input("Enter the name of your second favorite movie : ")
var3=input("Enter the name of your third favorite movie : ")
list=[var1, var2, var3]
print(list)
'''

# Q2. Write a program to check if a list contains a palindrome of elements.

var1=[1, 2, 1]
var2=[1, 2, 3]
var3=var1.copy()
var3.reverse()
if(var3 == var1):
    print("The number given by you is palindrome !")
elif(var3 != var1):
    print("The number given by you is not an palindrome !")

# Q3. Write a program to count the number of students in the following tuple .

var1=("C", "D", "A", "A", "B", "B", "A")
var2=var1.count("A")
print(var2)

# Q4. Store the above values in a list and sort them from A to D .

var1=["C", "D", "A", "A", "B", "B", "A"]
var2=var1.sort()
print(var1)


