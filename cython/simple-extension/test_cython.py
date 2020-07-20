# coding: utf-8
from  cyt_module import subtract
subtract(2,2)
subtract(2,-2)
subtract(-2,-2)
subtract(-2,2)
a=subtract(-2,2)
type(a)
a=subtract(-2,2.)
type(a)
import numpy as np
c=np.arange(10)
d=c+2.1
np.random.shuffle(c)
np.random.shuffle(d)
a=subtract(c,d)
a
c=1j
a=subtract(c,d)
a
