import numpy as np

array = np.array([[1,2,3],
                 [4,5,6]])

array1 = np.array([[1,2,3],
                 [4,5,6]])
print(array)
print('number of dim':,array.ndim)
print('shape':,array.shape)
print('size:',array.size)
print(np.argmin(array)) #找出最小索引
print(np.cumsum(array)) #逐項加起來
print(np.transpose(array))  #轉置
print(np.clip(array,5,9))   #小於5的變5大於9的變9
print(np.vstack((array,array1)))  #上下合併
print(np.hstack((array,array1)))  #左右合併
print(np.split(array,2,axis=1))  #分割成兩列 axis=1 is row  axis=0 is column

array3 = array*array1   #個別乘
np.dot(array,array1)    #矩陣乘法

np.sum(array3)  #find sum
np.sum(array3,axis=0)  #find sum in row1
np.min(array3)  #find min
np.min(array3,axis=0)  #find min in row1
np.max(array3)  #find max
np.max(array3,axis=0)  #find max in row1

