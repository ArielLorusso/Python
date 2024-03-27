import numpy as np
import timeit
import time


def while_test (n=1000) -> int:
    a = 1
    while n > 0 :
        n -=1
        a +=n 
    print(a)
    return 
def for_test (  n=1000):
    a = 1
    for i in range (n):
        n -=1
        a +=n 
    print(a)
    return 
def for_typed (  n:int =1000 ) -> int:
    a:int = 1
    for i in range (n):
        n -=1
        a +=n 
    print(a)
    return 0
def numpy_test( n=1000):
    i = np.arange(0, n)
    a = np.sum(i)
    return print(a)
     


def main():
    n=1000
    t = timeit.timeit(  f'while_test ({n})', globals=globals(), number=1)
    print(           f'\t while_test: {t} seconds ')

    t = timeit.timeit( f'for_test({n})',globals=globals(),  number=1)
    print(         f' \t for_test: {t} sec ')
    
    t = timeit.timeit( f'for_typed({n})',globals=globals(), number=1)
    print(         f' \t for_typed {t} sec ')

    t = timeit.timeit( f'numpy_test({n})',globals=globals(), number=1)
    print(         f' \t numpy_test: {t} sec ')

if __name__ == "__main__":
    main()