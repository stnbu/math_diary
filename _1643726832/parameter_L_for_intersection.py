"""
Elliptic Tales sure likes its polynomials. Thoroughly understanding polynomials is helpful.

Let's.
"""

"""
The most compact pythonic representation of a polygon is (bold claim)...

polynomial = {
    frozenset([(x, n), (y, m), ...(z, p)]): coefficient,
    ...
}

UPDATE: replace frozenset with frozendict

Where the variables are [x, y ...z] and the powers/exponents are [n, m ..p].

Each item in the dictionary is a monomial term.

Examples:

x**2 - yz --> {
    frozenset([(x, 2)]): 1,
    frozenset([(y, 1), (z, 1)]): 1
}

x**3 + a**x + b - y**2 --> {
    frozenset([(x, 3)]): 1,
    frozenset([(x, 1)]): a,
    frozenset(): b,
    frozenset([(y, 2)]): -1,
}

Let's try sum.
"""

from itertools import product
from frozendict import frozendict

fs = frozenset
fd = frozendict


def add(p0, p1):
    results = {}
    common_terms = set(p0) & set(p1)
    p0_ = p0.copy()
    p1_ = p1.copy()
    for key in common_terms:
        results[key] = p0[key] + p1[key]
        p0_.pop(key)
        p1_.pop(key)
    results.update(p0_)
    results.update(p1_)
    return {v: c for (v, c) in results.items() if c != 0}


# for now... define just field element (e.g. 3.95/aka float) multiplication
def mul(p0, r):
    results = {}
    for key, coeff in p0.items():
        results[key] = coeff * r
    return results


# which permits us to define sub as
def sub(p0, p1):
    return add(p0, mul(p1, -1))


def _get_symbol(sym, symbol_pows):
    for symbol, power in symbol_pows:
        if sym == symbol:
            return sym, power


def mul(p0, p1):
    results = {}
    for (vars0, coeff0), (vars1, coeff1) in product(p0.items(), p1.items()):
        vars0 = dict(vars0)
        vars1 = dict(vars1)
        new_vars = []
        for symbol in set(vars0) | set(vars1):
            power = vars0.get(symbol, 0) + vars1.get(symbol, 0)
            new_vars.append((symbol, power))

        results[fs(new_vars)] = coeff0 * coeff1
    return results

if __name__ == "__main__":

    for v in 'abcdefghijklmnopqrstuvwxyz':
        globals()[v] = v

    p0 = {frozendict([(x, 2)]): 3, frozendict([(y, 1)]): 1}
    p1 = {frozendict([(x, 2)]): 2, frozendict([(y, 1)]): 1}
    assert add(p0, p1) == {frozendict({'y': 1}): 2, frozendict({'x': 2}): 5}
