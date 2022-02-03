from sympy import *
from sympy.plotting import plot_implicit

x, y = symbols("x y")

plot = plot_implicit(Eq(x ** 3 - y, 0), show=False, backend="matplotlib")

from btools import print_svg

print_svg(plot)
