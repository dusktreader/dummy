#! /usr/bin/env python
#
# \Dropbox\Reasearch_Nguyen\Dummy\tests
# Hoang Long Nguyen (hn269@cornell.edu)
# 2014/03/28
#
# 
"""
The Python Documentation and Release Project
============================================

Introduction
------------

This project is an attempt at documenting Python code and prepare a ready-to-
release Python package, including proper tests and documentations. The ultimate 
goal of this project is to release a Python package of John A. Marohn 
(jam99@cornell.edu) onto GitHub and PyPI.

The dummy package
-----------------

This package is literally a dummy package. All it does is adding or subtracting 
two given numbers and give out a result.

"""

def add(n1,n2):
    result = 0
    result = n1+n2
    return result

def sub(n1,n2):
    result = 0
    result = n1-n2
    return result