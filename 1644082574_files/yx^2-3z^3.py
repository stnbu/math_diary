import sys
from sympy import *
from sympy.plotting import plot_implicit

x, y, z = symbols("x y z")
if sys.argv[1] == 'x':
    x = 1
if sys.argv[1] == 'y':
    y = 1
if sys.argv[1] == 'z':
    z = 1

eq = Eq(y*x**2 - 3*z**3, 0)

plot = plot_implicit(
    eq, show=False, backend="matplotlib", line_color="black"
)

import btools
btools.print_svg(plot)
