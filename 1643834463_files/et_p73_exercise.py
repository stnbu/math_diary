from sympy import *
from sympy.plotting import plot_implicit, plot
from sympy.plotting.plot import Plot, Parametric2DLineSeries, LineOver1DRangeSeries
from sympy.plotting.plot_implicit import *

x, y, t = symbols("x y t")

from sympy import *
from sympy.plotting import plot_implicit

x, y = symbols("x y")

plot(Eq(x ** 2 + y + 4, 0), (2 * t + 1, t - 5), backend="matplotlib")

f_plot = plot_implicit(
    Eq(x ** 2 + y + 4, 0),
    xvar=(x, -5, 5),
    yvar=(y, -8, 2),
    show=False,
    backend="matplotlib",
)
l_plot = plot_parametric(
    (2 * t + 1, t - 5),
    xlim=(-2.5, 2.5),
    ylim=(-8, -2),
    show=False,
    backend="matplotlib",
)
l_plot.extend(f_plot)

l_plot.show()
# import btools ; btools.write_svg_to_file(plot, __file__ + ".svg")
