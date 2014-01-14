#!/usr/bin/env python

from distutils.core import setup, Extension

module1 = Extension('hello',
                    sources = ['hello.c'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1])
