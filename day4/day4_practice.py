# Q1. Store following word meanings in a python dictionary :

# table : "a piece of furniture", "lists of facts and figures " ; cat : "a small animal"

var1= {
    "cat" : " A small animal",
    "table" : [" A piece os furniture ", "list of facts and figures " ]
}
print(var1)

# Q2. You are given a list of subjects for students. Assume one classroom is required for 1 subject.How many classroom are needed by all students.

# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

var1= {
    "python", "java", "python", "javascript", "java",
    "python", "java", "C++", "c"
}
print(len(var1))

# Write a program to enter the marks of three subjects from the user and store them in a dictionary and add one by one. Use subject name as a key and marks as value.

marks={}

x = int(input("Enter your marks of physics : "))
marks.update({"physics" : x})

x = int(input("Enter the marks of mathematics : "))
marks.update({"maths" : x})

x = int(input("Enter your marks of chemistry : "))
marks.update({"chemistry" : x})

print(marks)