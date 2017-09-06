# This program contains functions that evaluate formulas used in geometry.
#
# Dammorah Jennings
# September 5, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a
def circle_area(r):
    a= math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

# my attempt

def parallelogram_area(b, h):
    a = b * h
    return a
def trapezoid_area(x, b, h):
    a = ((x + b)/2) * h
    return a
def rectangular_prism_volume(w, h, l):
    v = w * h * l
    return v
def cone_volume(r, h):
    v = math.pi * r**2 * (h/3)
    return v
def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v
def rectangular_prism_surface_area(w, l, h):
    a = 2(w * l + h * l + h * w)
    return a
def sphere_surface_area(r):
    a = 4 * math.pi * r**2
    return a
def right_triangle_hypotenuse(a, b):
    c = (math.sqrt(a**2 + b**2))
    return c
