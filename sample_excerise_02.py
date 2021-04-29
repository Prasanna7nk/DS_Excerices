# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

"""
Write a NumPy program to find the number of elements
of an array, length of one array element in bytes and total
bytes consumed by the elements.
"""
import numpy as np

array = np.array([2, 1, 1, 0, 9, 7, 3, 6, 9, 4, 2])

print(f"Number of elements in the array: {array.size}")
print(f"Length of one array element: {array.itemsize} bytes")
print(f"Total Bytes conusmed: {array.nbytes} bytes")
import numpy as np

a = np.array([1,2,3,4,5])
print(a.size)

print(a.itemsize)

print(a.size * a.itemsize)


"""
Write a NumPy program to find the set difference of two
arrays. The set difference will return the sorted, unique
values in array1 that are not in array2.
"""
import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 2, 1, 1, 0, 9, 7, 3, 6, 9, 4, 2])
array2 = np.array([8, 5, 4, 2, 3, 6, 7, 8, 2])

set_difference = np.setdiff1d(array1, array2)
print(set_difference)




a = np.array([5,4,3,2,1])

b = np.array([2,3,4,6])

print(np.setdiff1d(a,b))


"""
Write a NumPy program to compute the cross product
of two given vectors.
"""
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[2, 3, 4], [4, 5, 6]])

cross_product = np.cross(arr1, arr2)
print(cross_product)

A = np.array([5,6,7])
B = np.array([1,2,3])
output = np.cross(A,B)
print(output) 



"""
Write a NumPy program to compute the determinant of
a given square array
"""
import numpy as np

sq_arr = np.array(
    [
        [
            [1, 2, 3],
            [2, 3, 4],
            [5, 6, 7]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [8, 4, 0]
        ],
        [
            [8, 9, 1],
            [5, 6, 3],
            [6, 2, 7]
        ]
    ]
)

det = np.linalg.det(sq_arr)

print(det)
arr = np.array([[6,1,1],[4,-2,5],[2,8,7]])
output_det = np.linalg.det(arr)
print(output_det)


"""
Write a NumPy program to compute the eigenvalues and
right eigenvectors of a given square array.
"""
import numpy as np

sq_arr = np.array([[1, 2], [6, 9]])

eigen_vals, eigen_vectors = np.linalg.eig(sq_arr)
print(f"Eigen Values: {eigen_vals}")
print(f"Eigen Vectors: {eigen_vectors}")
arr = np.array([[6,1,1],[4,-2,5],[2,8,7]])
w,v = np.linalg.eig(arr)
print("eigenvalue",w)
print("eigenvector",v)


"""
Write a NumPy program to multiple three matrices each
of 3*3 dimensions.
"""
import numpy as np

A = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [5, 6, 7]
])

B = np.array([
    [5, 6, 7],
    [9, 8, 2],
    [6, 6, 6]
])

C = np.array([
    [5, 3, 2],
    [0, 0, 0],
    [6, 3, 4]
])

ABC = np.matmul(np.matmul(A, B), C)  # (A x B) x C

print(ABC)

arr = np.random.randint(0,10,size=(3,3))
a2 = np.random.randint(0,10,size=(3,3))
a3 = np.random.randint(0,10,size=(3,3))

print(np.matmul(np.matmul(a3,a2),arr))


print(np.dot(np.dot(a3,a2),arr))



