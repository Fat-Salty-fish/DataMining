import numpy as np
import matplotlib.pyplot as plt


file = open('magic04.txt')
Data = [[float(i) for i in a.split(',')[:-1]] for a in file.readlines()]
mymatrix = np.array(Data)
mymean = np.mean(mymatrix, axis=0)
print(mymean)
print('\n')

mean1=np.transpose(mymean)
n = mymatrix.shape[0]
temp=[1 for i in range(n)]
tm=np.matrix(temp)
tm = np.transpose(tm)
temp1=tm*mean1
z= mymatrix - temp1
zt=np.transpose(z)
inner=zt*z/3
print(inner)
print('\n')

Sum=0
zp=[0 for i in range(n)]
for i in range(n):
  zp[i]=np.transpose(z[i])
  temp2=zp[i]*z[i]
  Sum+=temp2
Sum=Sum/3
print(Sum)
print('\n')



