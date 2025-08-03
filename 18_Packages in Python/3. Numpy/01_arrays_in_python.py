import numpy as np

# Create a numpy array
Array=np.array([1,2,3,4,5])

#perform basic operations
print("array:",Array)
print("mean:\n",np.mean(Array))
print("median:\n",np.median(Array))
print("add:",np.sum(Array))

# createe 2-d array
matrix1=np.array([[1,3,5],[2,4,6]])
print("2-D Matrix:\n",matrix1)
print("Mean of the Matrix:\n",np.mean(matrix1))
print("transpose of the matrix:\n",np.transpose(matrix1))

# create 3-D array
matrix=np.array([[1,2,3],[6,7,8],[9,8,7]])
print("3-D Matrix:\n",matrix)
print("transpose:\n",np.transpose(matrix))
print("element addition:\n",matrix+5)
