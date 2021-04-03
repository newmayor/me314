import sympy as sym
from sympy.abc import x,y,z,t,s 
from sympy import Matrix
from sympy import Function, Symbol
from sympy import diff, integrate

t = Symbol('t')
s = Symbol('s')
f = Function('f')(s)
g = Function('g')(s)

w = Matrix([x, y, z])
X = w.T*w 
diffX = (w.T*w).jacobian(w) 
print('\nX is ', X)
print('\nThe derivative of X is ', diffX)
print('')

Y = (f**2)