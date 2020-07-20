import numpy as np
#import memory_profiler

#@profile
def my_func1():
    a = np.random.random((3000, 3000))
    b = np.random.random((3000, 3000))
    c = 2.0 * a - 4.5 * b + np.sin(a) - np.cos(b)#*
    return c

#@profile
def my_func2():
    a = np.random.random((3000, 3000))
    b = np.random.random((3000, 3000))
    c = (2.0 * a - 4.5 * b) + (np.sin(a) - np.cos(b))
    return c

#@profile
def my_func3():
    a = np.random.random((3000, 3000))
    b = np.random.random((3000, 3000))
    c = 2.0 * a 
    c -= 4.5 * b 
    c += np.sin(a) 
    c -= np.cos(b)
    return c

if __name__ == '__main__':
    my_func1()
    my_func2()
    my_func3()
