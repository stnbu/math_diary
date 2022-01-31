
from sympy import *
from sympy.plotting import plot_implicit

eq = lambda x, y: x * y - 1

x, y = symbols('x y')
p1 = plot_implicit(Eq(x * y - 1), backend='matplotlib')

