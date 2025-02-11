#assignment 4
#q1
import numpy as np
arr=np.array([4,1,2,5,1])
print(arr)
arr=arr+2
print(arr)
arr=arr-2
arr=arr*3
print(arr)
arr=arr/2
print(arr)
#q2
arr=([1,2,3,6,4,5])
print(arr)
revarr=arr[::-1]
print(revarr)
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ]) 
mf = np.bincount(x).argmax()
print ("most frequent value is ",mf,"with indices" )
for i in range(0,10):
    if x[i]==mf:
        print(i)
mff=mf = np.bincount(y).argmax()
print ("most frequent value is ",mff,"with indices" )
for j in range(0,10):
    if y[j]==mff:
        print(j)
#q3
brr=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(brr[0,1])
print(brr[2,0])
#q4
asrar=np.linspace(10,100,25)
print(asrar.ndim)
print(asrar.shape)
print(asrar.size)
print(asrar.dtype)
print(asrar.nbytes)
transpose=asrar.reshape(25,1)
print(transpose)
#no we cant do same with the t attribute coz there is no transpose defined for a 1 d array

#q5
ucs420asrar=np.array([[10,20,30,40],[50,60,70,80],[90,15,20,35]])
print(np.mean(ucs420asrar))
print(np.median(ucs420asrar))
print(np.max(ucs420asrar))
print(np.min(ucs420asrar))
print(np.unique(ucs420asrar))
reshapeducs420asrar=ucs420asrar.reshape(4,3)
print(reshapeducs420asrar)




