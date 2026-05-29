import numpy as np
a=[1,2,3,4]
x=np.array(a)
print(x.ndim)
print(x.shape)
x=x.reshape(2,2)
x.shape
print(x)
type(x)

a=np.arange(10,dtype=np.int16)
b=np.arange(10,dtype=np.int16)
a.dtype
a.shape
a.ndim

a=np.arange(5)
b=np.arange(5)
print(a+b)
print(a-b)
print(np.sign(a))
print(np.cos(a))
print(id(x))