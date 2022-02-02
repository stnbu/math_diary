
# pip install git+https://github.com/stnbu/polynomier.git@d023fa334c93683db7db480b0350e0d81f7ece80

# see p73 of https://www.amazon.com/Elliptic-Tales-Curves-Counting-Number/dp/0691163502/

from polynomier import MultiPoly, fd
from polynomier.symbols import *

f = MultiPoly({fd({x: 2}): 1, fd({y: 1}): 1, fd(): 4})
g_x = MultiPoly({fd({t: 1}): 2, fd(): 1})
g_y = MultiPoly({fd({t: 1}): 1, fd(): -5})

g = f.substitute(x, g_x).substitute(y, g_y)

print(g)