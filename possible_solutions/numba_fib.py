import numpy as np
import numba as nb

@nb.jit
def py_fib(n=4):
    p = np.zeros(n)
    p[1] = 1
    i = 2
    while i < n:
        p[i] = p[i-1]+p[i-2]
        i += 1
    return p

