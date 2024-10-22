#!/usr/bin/python

from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove('test.txt')
    
with suppress(FileNotFoundError):
    os.remove('t.txt')
    

os.remove('t.tex')
    