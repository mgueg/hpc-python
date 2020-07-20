# coding: utf-8
a=np.random.randint(10,size=16).reshape(4,4)
a=a.astype('float')
a[0:2,0:2]=0.21
a[1,:]
a[:1,:1]=0.21
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x
x[::2,1::2] = 1
get_ipython().run_cell_magic('timeit', '', 'arr = np.arange(1000)\ndif = np.zeros(999, int)\nfor i in range(1, len(arr)):\n    dif[i-1] = arr[i] - arr[i-1]\n    \n')
get_ipython().run_cell_magic('timeit', '', 'arr = np.arange(1000)\ndif = arr[1:] - arr[:-1]\n\n')
get_ipython().run_cell_magic('timeit', '', 'arr = np.arange(100)\ndif = np.zeros(99, int)\nfor i in range(1, len(arr)):\n    dif[i-1] = arr[i] - arr[i-1]\n    \n')
get_ipython().run_cell_magic('timeit', '', 'arr = np.arange(10000)\ndif = np.zeros(9999, int)\nfor i in range(1, len(arr)):\n    dif[i-1] = arr[i] - arr[i-1]\n    \n')
get_ipython().run_cell_magic('timeit', '', 'arr = np.arange(10000)\ndif = arr[1:] - arr[:-1]\n\n')
