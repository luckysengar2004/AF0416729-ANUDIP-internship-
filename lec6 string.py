#FIRST STRING PROGRAM
name="Lucky"
print(id(name))
name=name+"sengar"
print(name)

print("------------------------------------------")
#slicing on string
a="lucky sengar"
print(a)
print(a[1])
print(a[2])
print(a[1:10:2])
print(a[: :])   # give full string if we do not specify the start end and step

print("------------------------------------------")
#Slicing 2
a="I am learning python"
print("a[2:4]",a[2:4])
print("a[5:9]",a[5:9])
print("a[:15]",a[:15])
print("a[:]",a[:])
print("a[2:]",a[2:])
print("a[0:19:3]",a[0:19:3])
print("a[: :]",a[: :])
print("a[::-1]",a[: :-1])

#DELETE STRING
a = "lucky"
del a
print(a)'''

#is oprator - is operator is used to compare two objects and determine if they refer to the same memory location. 
'''x=["apple","banana"]
y=["apple","banana"]
z=x 
print(x is z)
print(x is y)

print("-------------------------------------------------")

# Capitalize() - used to make the first  char  in  upper case
str = "lucky sengar"
print(str)
print(id(str))
str = str.capitalize() # to capitalize store in different variable and then print.
print(str)
print(id(str))


#center()- used to align a string to the center by filling paddings to the left and right of the string.
str = "lucky sengar"
print(str)
str= str.center(15) # by default space 
print(str)
str1=str.center(15,'*') #you can also specify symbol
print(str1)

#count() - used to count element
str=" second a start index and third"
oc = str.count('a')
print(oc)
tc=str.count("a",8)
print(tc)
kc=str.count("a",3,8)
print(kc)

#endswith()-determines whether the string ends with a specified suffix, and returns True if it does, or False if it does not.
str=" second a start index and third"
isend=str.endswith('third')
print(isend)
ksend=str.endswith('nd',0,6)
print(ksend)

# startswith() - returns True if the string starts with the specified value, otherwise False.
str="second a start index and third"
str1=str.startswith("s")
print(str1)

# find() - The find() method in Python is used to locate the index of a substring within a string. It returns the index of the first occurrence of the substring, or -1 if the substring is not found.'str="second a start index and third"
str2=str.find('a')
print(str2)
str3=str.find('a',9,10)
print(str3)

#index() -  helps you find the index position of an element or an item in a string of characters or a list of items.
str="second a start index and third"
str2=str.index('a')
print(str2)
str3=str.index('a',9,13)
print(str3)

#isalnum() - aplha numeric -returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
str="1235421521515"
print(str.isalnum())

#isaplha() -  in python is a boolean function and hence has return values as either True or False
str="second a start index and third"
strr=str.isalpha()
print(str)

#isnumeric() - 
str="1235421521515"
print(str.isnumeric())

#islower - determines if all of the string's case-based characters (letters) are lowercase
str='hello'
str=str.islower()
print(str)

#lstrip() -  removes the leading whitespace
#rstrip() - used to return a new string by removing the trailing characters (based on the argument passed) from the input string
str=".....lucky....."
str1=str.lstrip('.')
str2=str.rstrip('.')
str3=str.strip('.')
print(str1)
print(str2)
print(str3)

#replace() - replaces a specified phrase with another specified phrase.
str="java is a programmming language java"
str=str.replace('java','c',2)
print(str)

#swapcase() - returns a string where all the upper case letters are lower case and vice versa.
str="java is a programmming language java"
str=str.swapcase()
print(str)



