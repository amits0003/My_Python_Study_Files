from distutils.core import setup, Extension

setup(name='NewExample',version='1.0',ext_modules=[Extension('helloworld', ['c_ex.c'])])
