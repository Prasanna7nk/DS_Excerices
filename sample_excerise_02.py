# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

import numpy as np

a = np.array([1,2,3,4,5])
print(a.size)

print(a.itemsize)

print(a.size * a.itemsize)


a = np.array([5,4,3,2,1])

b = np.array([2,3,4,6])

print(np.setdiff1d(a,b))


A = np.array([5,6,7])
B = np.array([1,2,3])
output = np.cross(A,B)
print(output) 


arr = np.array([[6,1,1],[4,-2,5],[2,8,7]])
output_det = np.linalg.det(arr)
print(output_det)

arr = np.array([[6,1,1],[4,-2,5],[2,8,7]])
w,v = np.linalg.eig(arr)
print("eigenvalue",w)
print("eigenvector",v)

arr = np.random.randint(0,10,size=(3,3))
a2 = np.random.randint(0,10,size=(3,3))
a3 = np.random.randint(0,10,size=(3,3))

print(np.matmul(np.matmul(a3,a2),arr))


print(np.dot(np.dot(a3,a2),arr))



