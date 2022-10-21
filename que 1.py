#We have to create an array of 15 elements between 1 & 20 using numpy
import numpy as np
Arr= np.random.randint(1,20,15)
print("Generated array:")
print(Arr)
#We have to reshape the array and print the reshaped array
Res=np.reshape(Arr, [3, 5])
print("Reshaped array: \n",Res)
#find the shape of the array
print("Shape of the array ",Res.shape)
# insert the max value with "0" in each row
for i in Res:
    i[i == max(i)] = 0
print(Res)