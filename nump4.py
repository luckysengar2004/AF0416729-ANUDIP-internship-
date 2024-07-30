# Spliting into equal sized sub arrays
'''import numpy as np
arr=np.array([1,2,3,4,5,6])

sub_arrays=np.split(arr,3)
for sub_arr in sub_arrays:
    print(sub_arr)'''

# Numpy sort
'''import numpy as np
arr=np.array([5,6,2,1,8,9])
sorted_arr=np.sort(arr)
print("Sorted array(ascending):-",sorted_arr)
sorted_arr_desc=np.sort(arr)[::-1]
print("Sorted array (descending):-",sorted_arr_desc)'''

# 
'''import numpy as np
matrix=np.array([[5,6,2,1,8,9],[5,8,92,4,100,5]])
sorted_matrix=np.sort(matrix,axis=1)
print("Sorted matrix (ascending along rows):-")
print(sorted_matrix)
'''

#concatenate two array
'''import numpy as np
arr=np.array([[1,2],[3,4]])
arr1=np.array([[5,6],[7,8]])
result=np.concatenate((arr,arr1),axis=1)
print(result)'''

# hstack
'''import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = np.hstack((arr1,arr2))
print(result)

# Vstack
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = np.vstack((arr1,arr2))
print(result)'''

# MEAN , VARIENCE AND STANDARD DEVIATION
'''import numpy as np

classB=np.array([70,80,85,95,100])
classB_mean=np.mean(classB)

print("class B Score Average:-  ",classB_mean)

variable=np.var(classB)
print("Class B varience is:-",variable)

standard=np.std(classB)
print("Standarad deviation:-",standard)'''

# Median(50th Percentile)
'''import numpy as np
test_scores=([65,7,5,85,96,75,52,52,74,12,63,100,52,85,45,85,96,42,12,85,95,42,84,90,52,42,95,75,42,62,42])
Q1=np.percentile(te,st_scores,50)
print("Median (50th percentile)",Q1)
'''
#percentile
'''import numpy as np
# Test scores of 30 students
test_scores = np.array([65, 75, 80, 85, 90, 92, 94, 95, 96, 98, 100, 102, 104, 106, 108,
110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138])
q1 = np.percentile(test_scores, 25)
print("Lower Quartile (25th Percentile):", q1)'''

# np.load() # loading and saving file
import numpy as np
scores=np.array([55,52,63,84,95,75])
np.save("Student_scores.npy",scores)
loaded_scores=np.load("student_scores.npy")
print("original Scores:-", scores)
print("Loaded Scores:- ",loaded_scores)




