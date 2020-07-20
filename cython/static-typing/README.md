## Using static typing 

Continue with the simple Cython module for subtracting two numbers:
```
def subtract(x, y):
    result = x - y
    return result
```

Declare the function internal variable `result` as integer. Try to call the
function with different types of arguments (integers and floats), what kind of
results you do get?

Next, declare also the function arguments as integers, and rebuild the module 
(Note: if working with interactive interpreter you need to exit or
reload the module). What happens when you now call the function with
floating point arguments?

Finally, try to declare arguments as floating point numbers (while keeping
`result` as integer), what happens?

### MG Notes

How to annotate and view cython code (with additional lines added by cython 

```shellscript

cameleon:cython mik$ cython -a mandel_cyt.pyx
cameleon:cython mik$ ls -lhrt mandel_cyt.html
-rw-r--r-- 1 mik admin  58K 17 mai 23:06 mandel_cyt.html

```
