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

def add(p0, p1):
    results = {}
    common_terms = set(p0) & set(p1)
    for key in common_terms:
        results[key] = p0[key] + p1[key]
        p0.pop(key)
        p1.pop(key)
    results.update(p0)
    results.update(p1)
    return results
        