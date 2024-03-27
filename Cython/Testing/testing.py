import np_Cython_py
import timeit

cy = timeit.timeit('np_Cython_cy.main()',
                   setup='import np_Cython_cy',
                   number=1)


#py = timeit.timeit('np_Cython_py.main()',
#                   setup='import np_Cython_py',
#                   number=1)

print(cy)