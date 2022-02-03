from sympy import *
from sympy.plotting import plot_implicit, plot
from sympy.plotting.plot import Plot, Parametric2DLineSeries, LineOver1DRangeSeries
from sympy.plotting.plot_implicit import *
x, y, t = symbols("x y t")


f_series = ImplicitSeries(
    Eq(x**2 + y + 4, 0),
    var_start_end_x=(x, -5, 5),
    var_start_end_y=(y, -8, 2),
    has_equality=True,
    use_interval_math=True,
    depth=0,
    nb_of_points=300,
    line_color='blue')

plot_expr = [(2*t + 1, t - 5, (t, -10, 10))]
l_series = [Parametric2DLineSeries(*arg) for arg in plot_expr]

plot_expr = [(4*t**2 + 5*t, (t, -10, 10))]
g_series = [LineOver1DRangeSeries(*arg) for arg in plot_expr]

p = Plot(f_series, *l_series, *g_series, xlim=(-5, 5), ylim=(-8, 2), labels=True)

from btools import *
#import ipdb; ipdb.set_trace()
write_to_file(p, __file__ + ".svg")
#print('done')