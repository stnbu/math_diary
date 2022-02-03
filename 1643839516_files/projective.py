from sympy import *
from sympy.plotting import plot_implicit

x, y = symbols("x y")

plot = plot_implicit(Eq(x**3 - y, 0), show=False, backend="matplotlib")

# do not look below this line!
import sys
import io
backend = plot.backend(plot)
backend.process_series()
f = io.StringIO()
backend.fig.savefig(f, format="svg")
f.seek(0)
print(f.read())
