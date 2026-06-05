# Lists and Tuples.

# LISTS 
# A built in data type that stores a set of values .
# It can store elements of different types (Integer, float, string, etc.)
# for use : "[]"

marks1=94.4
marks2=87.5
marks3=95.2
marks4=66.4
marks5=45.1

marks=[94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))

# It also starts from 0 to infinity .
# In the this function we can also take out specific value in our list .
# For Example : 

print(marks[0])
print(marks[1])

# Lists are changeable but in some cases.
# for example the following code we will run would be syntax error as we can't change the value in it through other variable.

'''str = "hello"
print(str[0])
str[0]="Y"'''
# But the following code which will be presented right now would'nt be an syntax error as we would commit the change in other variable only but in other variable but before the print option.

# LIST SLICING.

# List slicing is an easy topic and it has no new syntax formula 
# SYNTAX : list_name[ starting_idx : ending_idx ]

marks=[85,94.76,63,48]
print(marks[:4 ])

# List methods

# The function " list.append() " is an function which adds one element at the end .

list=[2,1,3]
list.append(4)
print(list)

# The function "list.sort()" is an function which sorts all values in an ascending order .

list=[2, 3, 1]
print(list.sort(reverse=False))
print(list)

# The function "lis.reverse" function which is used for reversing the list.
# For example :

list=['a', 'b', 'c', 'd', 'e', 'f']
list.reverse()
print(list)

# The "list.insert(idx, el) is an function that inserts an element at index.
# for example :

list=[2, 1, 3]
list.insert(1, 5)
print(list)

# The "list.remove()" function is an function which removes first occurrence of element
# For example :

list=[2, 1, 3]
list.pop(1)
print(list)
