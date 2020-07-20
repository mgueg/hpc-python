# coding: utf-8
c=np.arange(64).reshape(8,8)
np.random.shuffle(c)
a,b=np.split(c,2)
a.shape
d=np.vstack((a,b)
)
np.all(c==d)
