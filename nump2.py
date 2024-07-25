#access Diagonal elements
'''import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.diag(arr))
print("----------------------------------------------------")
print("Inserting elemts in diagonal in an array")
print(np.diag((3,5,9)))'''

'''import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])'''

#randint()- 
'''import numpy as np
rand=np.random.rand(4)
print(rand)
rand=np.random.rand(2,3)
print(rand)
rand=np.random.randint(0,100,12)
print(rand)'''

#re shape
'''import numpy as np

arr=np.random.randint(0,100,12)
print(arr)
arr=arr.reshape(4,3)
print(arr)
print("Array Values is:- ",arr[0][1])
print("Array Values is:- ",arr[1][0])
print(arr.shape)
arr=arr.reshape(-1,4)
print(arr)
arr=arr.reshape(2,-1)
print(arr)'''

#Seed
'''import numpy as np

np.random.seed(145)
arr=np.random.randint(0,100,30)
arr=arr.reshape(6,5)
print(arr)
print(arr[2:,2:])
print(arr[3:5,2:4])'''

#Question
'''import numpy as np
arr=np.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing=arr[4:9]
print("new slicing" ,slicing)
print("new array",arr)
print(type(slicing))
print(type(arr))
slicing[:]=0
print("old slicing",slicing)
print("old array",arr)'''

#printing even numbers
'''import numpy as np
arr=np.arange(1,15)
print(arr)
print(arr[arr%2==0])'''

#ARANGE FUNCTION:- 
'''import numpy as np
arr=np.arange(1,15)
print(arr)
print(arr[arr%2==0])
print(arr[arr%2!=0])
print(arr[arr>8])
arr[arr%2==0]=0
print(arr)
arr=np.arange(1,8)
print("--------")
print(arr+2)
print("--------")
print(arr*2)
print("--------")
print(arr**2)'''

#   
'''import numpy as np
arr=np.array([10,20,30,4,5])
print("-----------")
print(np.min(arr))
print("-----------")
print(np.max(arr))
print("-----------")
print(np.sin(arr))
print("-----------")
print(np.cos(arr))
print("-----------")
print(np.argmin(arr))
print("-----------")
print(np.argmax(arr))
print("-----------")
print(np.sqrt(arr))'''

'''import numpy as np
np.random.seed(122)
mat=np.random.randint(1,29,9).reshape(3,3)
print(mat)
print(np.sum(mat))
print(np.cumsum(mat))
print(np.min(mat))
print(np.max(mat))
print("-------ROW WISE--------")
print("SUM IS",np.sum(mat,axis=1))
print("--------------------")
print("MIN IS",np.min(mat,axis=1))
print("--------------------")
print("MAX IS",np.max(mat,axis=1))
print("--------------------")
print("CUMSUM IS",np.cumsum(mat,axis=1))
print("------COLUMN WISE------")
print("SUM IS",np.sum(mat,axis=0))
print("--------------------")
print("MIN IS",np.min(mat,axis=0))
print("--------------------")
print("MAX IS",np.max(mat,axis=0))
print("--------------------")
print("CUMSUM IS ",np.cumsum(mat,axis=0))'''

# UNIQUE 
import numpy as np

np.random.seed(122)
mat=np.random.randint(1,21,10)
print(mat)
np.random.shuffle(mat)
print(mat)
print(np.unique(mat,return_index=True,return_counts=True))
print(np.unique(mat).size)


