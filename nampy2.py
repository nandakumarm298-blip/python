
import numpy as np
# copy the array
arr=np.array([10,20,30,40,50])
x=arr.copy()
print(x)
arr[0]=42
x=arr.copy()
print(x)


# Reshaping
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)


arr=np.array([1,2,3])
for x in arr:
    print(x)


arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)




arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)



