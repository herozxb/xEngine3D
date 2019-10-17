#! /usr/bin/env python
import math
import numpy as np

class vector3d(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def return_array(self):
        return [self.x, self.y, self.z]
        
class triangle(object):
    def __init__(self, lines):
        self.line1 = lines[0]
        self.line2 = lines[1]
        self.line3 = lines[2]

class mesh(list):
    
    def __delitem__(self, key):
        self.__delattr__(key)
    def __getitem__(self, key):
        return self.__getattribute__(key)
    def __setitem__(self, key, value):
        self.__setattr__(key, value)
        
        
        

