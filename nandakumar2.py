import numpy as np

arr=[10,20,30,40]
print(arr)
print(type(arr))

arr1=np.array([arr])
print(arr1)
print(type(arr1))

# Dimensions in array
arr=np.array(10)
print(arr)
print(arr.ndim)
arr1=np.array([10,210,30,40])
print(arr1)
print(arr1.ndim)
arr2=np.array([[10,20,30,40],[1,2,3,4]])
print(arr2)
print(arr2.ndim)
