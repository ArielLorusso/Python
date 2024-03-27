import timeit

import numpy as np
cimport numpy as np  # Import the numpy C library
# Define the data type
ctypedef np.int32_t DTYPE_t

def while_test (n=1000) -> int:
    i = np.arange(0, n)
    a = np.sum(i)
    print(a)
    return 

cpdef int  for_typed ( long n )  :     # OPTIMIZED
    cdef long a = 0
    cdef int i = 0
    for i in range (n):
        n -=1
        a +=n 
    print(a)
    return 0

cpdef int  numpy_test( long n ):
    i = np.arange(0, n)
    a = np.sum(i)
    print(a)
    return 0

cpdef int numpy_typed ( long n ) :
    cdef np.int32_t[:] i = np.arange(0, n, dtype=np.int32)
    cdef long a = np.sum(i)
    print(a)
    return a
#


def main():
    n=1000000
    t = timeit.timeit(  f'while_test ({n})', globals=globals(), number=1)
    print(           f'\t while_test_C: {t} seconds ')

    t = timeit.timeit( f'for_typed({n})',globals=globals(), number=1)
    print(         f' \t for_typed_C: {t} sec ')
    
    t = timeit.timeit( f'numpy_typed({n})',globals=globals(), number=1)
    print(         f' \t numpy_typed_C {t} sec ')

    t = timeit.timeit( f'numpy_test({n})',globals=globals() , number=1)
    print(         f' \t numpy_test_C: {t} sec ')
