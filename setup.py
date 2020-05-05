from setuptools import setup, Extension

from Cython.Build import cythonize

ext_modules = cythonize([
    Extension("base64N", ["base64N.py"]),
    Extension("stdbase64", ["stdbase64.py"])
])

setup(
    ext_modules=ext_modules
)
