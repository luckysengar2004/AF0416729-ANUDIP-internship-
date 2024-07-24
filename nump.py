#first program using numpy
import numpy as np
a = np.array (42)
b = np.array([1, 2, 3, 4, 5])
c= np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("a array ",a)
print("b array ",b)
print("c array ",c)
print("d array ",d)
print("a array dimen ",a.ndim)
print("b array dimen",b.ndim)
print("c array dimen",c.ndim)
print("d array dimen",d.ndim)

#second program - Access array element
import numpy as np
arr=np.array([1,2,3,4])
print(arr[3])

#slicing
import numpy as np
arr=np.array([1,2,3,4])
print(arr[:2])

#slicing 2
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
sarr=arr[1:5]
print(arr)
print(sarr)
sarr[2]=100
print(arr)
print(sarr)

#copy operation
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr.copy()
arr[0]=45
print(arr)
print(x)

#view
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr.view()
arr[0]=45
print(arr)
print(x)

#zeroes
import numpy as np
a=np.zeros(6)
print(a)
b=np.zeros([6,2])
print(b)

#numpy.zeros with shape
import numpy as np
a=np.zeros((6,2))
print(a)

#numpy.ones with shape
import numpy as np
b=np.ones((6,2))
print(b)

#create a 1d array of ones
import numpy as np
a=np.ones(6, dtype=int)

#an array with 6ones and integer data type
b=np.ones((6,), dtype=int)

#create 2d array with ones
c=np.ones([4,2])
print(a)
print(b)
print(c)

#EYES
arr4=np.eye(3)
print(arr4)
arr4=np.eye(3,4)
print(arr4)

#Diagonal array
arr5=np.diag((3,4,5,6))
print(arr5)
print(arr5.ndim)
print(arr5.shape)






