import numpy as np
Arr=np.random.randint(1,20,(15))
print(Arr)

#Reshape the array to 3 by 5
Res=Arr.reshape(3,5)
print(Res)

#Print array shape
print(np.shape(Res))

#Replace the max in each row by 0
maxNum = np.amax(Res, axis=1)
print(maxNum)

d = np.where(np.isin(Res,maxNum), 0, Res)
print(d)
