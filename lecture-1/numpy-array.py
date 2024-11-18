import numpy as np

# initalization of numpy array
np1 = np.array([0, 1, 2, 3, 4, 5])
print(np1)

# to get number of elemeents in numpy array
print(np1.shape)

# arange function/property of numpy array if we use it and pass a range in parametes 
# it will initialize the numbers if given 3 it will initialize it like this ([0, 1, 2])
#only range defalut step = 1
np2 = np.arange(10)
print(np2)
# with step
np3 = np.arange(0, 10, 2)
print(np3)

#numpy's zeors func
np4 = np.zeros(10)
print(np4)

#numpy full func
np4 = np.full((10), 6)
print(np4)
