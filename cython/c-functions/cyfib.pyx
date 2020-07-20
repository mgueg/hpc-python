"""
Using pure C functions
If a function is used only within a Cython module, one can get rid of a large part of Python’s function call overhead by declaring the function as a pure C function, once again using the cdef keyword:

When a function is defined as a pure C function, it can be called only from the corresponding Cython module, but not from a Python code. If a function is called both from Cython and Python, Cython can generate an additional Python wrapper by declaring the function with cpdef instead of cdef
"""
# In [2]: %timeit cyfibonacci(30)
# 4.31 ms ± 54.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cpdef int fibonacci(int n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

# better than
# In [4]: %timeit cyfibonacci(30)
# 72.8 ms ± 1.33 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
#def fibonacci(int n):
#    if n < 2:
#        return n
#    return fibonacci(n-2) + fibonacci(n-1)
