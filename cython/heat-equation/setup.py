from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

include_path = [numpy.get_include()]
setup(
     ext_modules=cythonize("heat.pyx"),
     include_dirs=include_path
)
