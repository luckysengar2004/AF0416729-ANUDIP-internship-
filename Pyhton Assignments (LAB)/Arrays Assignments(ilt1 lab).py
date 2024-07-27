#Q-1- Convert the below list into numpy array that display the array input list my_list=[1,2,3,4,5]
import numpy as np

l=[1,2,3,4,5]
arr=np.array(l)
print(arr)

#Q-2- Convert the below list into numpy array that display the array than display the first and last index and then mutilpy each element by 2 and display the result input my_list=[1,2,3,4,5].
import numpy as np

l=[1,2,3,4,5]
arr=np.array(l)
n=len(arr)
print("First index:- ",arr[0])
print("Last index:-",arr[n-1])
print("Multiply the element by 2 :-",arr*2)

#------LAB 3 : -Working With Numpy ----------------
#Q-1 - Write a Numpy program to create an array of 10 zeroes , 10 ones , and 10fives.
import numpy as np

#zeroes
a=np.zeros(10)
print("An array of 10 ones:-",a)
#Ones
b=np.ones(10)
print("An array of 10 ones:-",b)
#fives
print("An array of 10 Fives:-",b*5)

#Q-2 - Write a Numpy program to create a 3X3 matrix with values ranging from 2 to 10
import numpy as np

arr1=np.arange(2,11).reshape(3,3)
print(arr1)







