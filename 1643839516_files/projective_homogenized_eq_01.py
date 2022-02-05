from sympy import *
from sympy.plotting import plot_implicit

x, y = symbols("x y")

def get_hp_for_some_z(z):
    return Eq(x**2 - y*z, 0)

affine_plot = plot_implicit(get_hp_for_some_z(1), show=False, backend="matplotlib", line_color="black")
for n in range(10, -1, -1):
    z = n/10  # z ranges [1,0] in increments of 0.1
    color = (1 - z, 0, 0)
    if z == 0:
        color = "green"
    straighter_plot = plot_implicit(get_hp_for_some_z(z), show=False, backend="matplotlib", line_color=color)
    affine_plot.extend(straighter_plot)

import btools; btools.print_svg(affine_plot)
