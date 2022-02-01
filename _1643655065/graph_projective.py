
from sympy import *
from sympy.plotting import plot_implicit

inf = 100

x, y = symbols('x y')

x_var = x, inf - 1, 1
y_var = y, inf - 1, 1


#p1 = plot_implicit(Eq(x * y - 1), backend='matplotlib')
#p1 = plot_implicit(Eq((inf/x) * (inf/y) - 1), backend='matplotlib')
p3 = plot_implicit(Eq((inf - y) - (inf - x)), x_var=x_var, y_var=y_var, backend='matplotlib')

"""
[Let's just say

>>> oo = 10*10

or something like that. Infinity!]


I _was_ working on trying to plot the two hemispheres of the sphere where (e.g.) the south
pole is just the regular x,y plane and the north pole has `oo,oo` as its "origin".

If the north hemisphere has x,y squished, say with `log(x),log(y)` then we can examine some
"huge" values as we near `oo,oo` and understand what infinity is doing.

Then I realized this won't get me very far with respect to "learning". It's just pretty pictures.

The interesting revelation is: if you homogenize `f` with a new `z` term and let `z` approach
zero, your `f` will transform into a straight line whose slope is the `[x : y : 0]` point you
are interested in.
"""

