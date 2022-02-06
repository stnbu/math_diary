from polynomier import Polynomial, fd
from polynomier.symbols import *

f = Polynomial({fd({x: 2}): 1, fd({y: 1}): 1, fd(): 4})
g_x = Polynomial({fd({t: 1}): 2, fd(): 1}) * -1
g_y = Polynomial({fd({t: 1}): 1, fd(): -5})

g = f.substitute((x, g_x), (y, g_y))

print(
    """
f(x, y) = {f}
x = {g_x}
y = {g_y}
f({g_x}, {g_y}) = {g}
""".format(
        f=f,
        g_x=g_x,
        g_y=g_y,
        g=g,
    )
)
