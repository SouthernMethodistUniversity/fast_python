def py_fib(n=4):
    p = [0, 1]
    while len(p) < n:
        p.append(p[-1]+p[-2])
    return p

%%cython
def cy_fib(int n):
    cdef int p[1000]
    cdef int len_p = 2
    p[0] = 0
    p[1] = 1
    if n > 1000:
        n = 1000
    while len_p < n:
        p[len_p] = p[len_p-1]+p[len_p-2]
        len_p += 1
    p_list  = [pi for pi in p[:len_p]]
    return p_list


