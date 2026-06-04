# Day 2, string and conditional statements
# String

#String is a data type that stores sequence of characters.

#Escape sequence characters are those characters that inserts 2 spaces in one string.
# '\n' is used to insert a new line in a string.
# '\t' is used to insert a tab in a string.
# 'len(str)' is used for getting to know the length of each string.
str1="punarv"
len1=len(str1)
print(len1)

str2="gupta"
len2=len(str2)
print(len2)

# sting concatination  used for make 2 strings an single string.

final_str= str1 + " " + str2
print(final_str)
print(len(final_str))

# indexing is used for knowing _ number charcter of in a string.

#the indexing of the character starts from zero.

str="punarvgupta"
ch=str[0]
print(ch)

# Caution in string indexing : in string we can accses that in in a specific what character if there but we can't change (manupilate) it.

str="punarv gupta"
str[4]="@"
print(str)

# This would be error as we can't manupilate characters in indexing.

# Slicing is majorly used in ML(Machine Learning) to acces parts of string
# For example : in "punarvgupta" we can use str(1 : 5) we can print the alfabets for 1 to 5.
# Caution = in slicing only the first alfabet ! would be showed not 5.

str="punarvgupta"
print(str[ 0 : 4 ])

# The 'endsWith())' function is an  function that responds to us in 'True' or 'False' tot tell that is there any last word in the substring .
# For Example : str.endsWith("er") help s to identify wether there is er in the last of an substring.
str="iamstudyingpython"
print(str.endsWith("ege"))
# The 'capitalize' function is an function which capatilizes the first alfabet of an string.

str="iamstudyingpython"
print(str.capatilize())
print(str)) 

# The "str.replace" function is an function which replaces all occurences of old values into new.

str="iamstudyingpython"
print(str.replace("o", "a"))

# this function can also replace words.

str="iamstudyingpython"
print(str.replace("python", "javascript"))

# The "str.find(word)" function is an function tht return's 1st index of 1st occurence

str="iamstudyingpython"
print(str.find(o))

# this function can also replace words.

# The "str.count()" counts the occurence of an substring

str="iamstudyingpython"
print(str.count("o"))


# CONDITIONAL STATEMENTS

# if-elif-else SYNTAX

# The "if" function is used to for condition .
# The "else" function is an function which is used for
# The "elif"(else if ) function is an function which used fo exeptions of if.
# For example : 


light="blue"
if("red")
    print("stop !")
elif("green")
    print(" Go !")  
elif("orange")
    print("Look !")
else:
    print("light is broken")          

