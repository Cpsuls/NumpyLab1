
import numpy as np
# 0.2
# m=np.random.randint(0,10,size=(8,10))
# print(m)
# n=np.sum(m,axis=0)
# mins=np.min(n)
# mins_index=np.where(np.sum(mins)==mins)
# print(m[mins_index])
# 0.3
# p1=np.arange(0,50)
# p2=np.arange(50,100)
# square = np.square(p1 - p2)
# s = np.sum(square)
# print(s)
# 0.4
# A = np.array([[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]])
# B=np.array([[3, -1], [2, 1]])
# C=np.array([[7, 21], [11, 8], [8, 4]])
# C=-1*C
# T=np.dot(C,B)
# X=np.linalg.solve(A,T)
# print(X)
# 1
# data=np.loadtxt(fname='minutes_n_ingredients.csv',max_rows=5,dtype='int32',delimiter=',',skiprows=1)
# print(data)
# 2
# print(np.amax(data[:,1],axis=0))
# print(np.amax(data[:,2],axis=0))
# print(np.amin(data[:,1],axis=0))
# print(np.amin(data[:,2],axis=0))
# print(np.median(data[:,1],axis=0))
# print(np.median(data[:,2],axis=0))
# 3
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# data[:,2]=np.clip(data[:,2],data[:,2],np.quantile(data[:,2],0.75))
# print(data)
# 4
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# num=np.count_nonzero(data[:,1]==0)
# data[:,1]=np.where(data[:,1]==0,1,data[:,1])
# print(data)
# 5
# print(len(np.unique(data,axis=1)))
# # 6
# print(np.unique(data[:,2]))
# print(len(np.unique(data[:,2])))
# 7
# data=data[(data[:,2:] <=5).all(axis=1)]
# print(data)
# 8
# np.set_printoptions(threshold=sys.maxsize)
# data1=[(data[:,1]//data[:,2])]
# print(data[:,1])
# print(np.amax(data1))
# 9
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# data_sorted=data[data[:,1].argsort()[::-1]]
# data_sorted=data_sorted[0:100]
# print(np.mean(data_sorted[:,2]))
# 10
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# num=np.random.choice(data.shape[0])
# print(data[num])
# 12 и 13
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# new_array=data[:,0]
# new_array=np.where(data,0,0)
# data=np.append(data,new_array,axis=1)
# data=data[:,[0,1,2,3]]
# print(data[:,2:])
# ex=np.logical_and(data[:,1]<20,data[:,2]<5)
# data[:,3]=np.where(ex,1,0)
# print(data)
# datax=data[:,3]
# num=np.count_nonzero(datax==1)
# print(num/len(datax)*100)
# 11
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# datan=data[:,2]
# n=np.mean(datan)
# nums=np.count_nonzero(datan<n)
# print(nums/len(datan)*100)
# 14
# massive=np.zeros((3,3))
# data=np.loadtxt(fname='minutes_n_ingredients.csv',dtype='int32',delimiter=',',skiprows=1)
# datao=data[:,1]
# datao=np.where(datao<10,1,datao)
# ex1=np.logical_and(datao>=10,datao<20)
# datao=np.where(ex1,2,datao)
# datao=np.where(datao>=20,3,datao)
# data2=data[:,0]
# datao=np.vstack([datao,data2])
# datao=np.transpose(datao)
# data3=data[:,2]
# zer=data[:,0]
# zer=np.where(zer,0,0)
# data3=np.vstack([data3,zer])
# data3=np.transpose(data3)
# datao=np.append(datao,data3,axis=1)
# datao=datao[:,[0,1,2]]
# print(datao)






