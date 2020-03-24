from itertools import repeat

def axpy(a, xi, yi):
    return a*xi+yi

def parallel_axpy(a, x, y, cores=1):
    pool = mp.Pool(processes = cores)
    result = pool.starmap(axpy, zip(repeat(a), x, y))
    return result

