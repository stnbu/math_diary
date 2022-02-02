# pip install git+https://github.com/stnbu/polynomier.git@19c9583
# see p73 of https://www.amazon.com/Elliptic-Tales-Curves-Counting-Number/dp/0691163502/

from polynomier import MultiPoly, fd
from polynomier.symbols import *

f = MultiPoly({fd({x: 2}): 1, fd({y: 1}): 1, fd(): 4})
g_x = MultiPoly({fd({t: 1}): 2, fd(): 1})
g_y = MultiPoly({fd({t: 1}): 1, fd(): -5})

g = f.substitute(x, g_x).substitute(y, g_y)

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
