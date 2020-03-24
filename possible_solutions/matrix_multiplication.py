def py_gemm(i):
    start = time.time()
    matrix_a = initialize_matrix(i, i, fill=1)
    matrix_b = initialize_matrix(i, i, fill=1)
    matrix_c = gemm(matrix_a, matrix_b)
    stop = time.time()
    return stop - start

def numpy_gemm(i):
    start = time.time()
    matrix_a = np.random.rand(i, i)
    matrix_b = np.random.rand(i, i)
    matrix_c = np.matmul(matrix_a, matrix_b)
    stop = time.time()
    return stop - start
    
def compare_gemm():
    for i in [500, 1000, 1500]:
        py_dt = py_gemm(i)
        numpy_dt = numpy_gemm(i)
        print("Size: {}, Speed-up: {}".format(i, py_dt / numpy_dt))

