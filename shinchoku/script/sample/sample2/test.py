#!/usr/bin/env python 

from math import* 

def euclidean_distance(x,y): 

return sqrt(sum(pow(a-b,2) for a, b in zip(x, y))) 

print euclidean_distance([0,3,4,5],[7,6,3,-1]) 
