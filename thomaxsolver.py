'''
Thomas-Algorithm refer to wiki: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
Here x in A x = d is solved.
the meaning of a b c in thomaxsolver.py is the same as those in wiki, that is 
  In A matrix:
    a is lower diagonal
    b is main diagonal
    c is upper diagonal
Note that: a b c have the same dimension and they are all zero-based in python, 
           so the terms a[0]=0 and c[-1]=0 should be added in a and c in order to 
           keep the same dimension with b and it is just for the convenience in calculation 
           without having any effect on the result.
If you have a tridiagonal matrix A which is difficult to get a b c, you can solve it with 
Python built-ins 'from scipy.linalg import solve_banded'.
'''
import numpy as np
def thomaxsolver(a,b,c,d):
    n = len(d)
    x = np.zeros(n)
    '''Calculate g_mod[]'''
    g_mod = [c[0] / b[0]]
    for j in range(1,n-1):
        gg = c[j] / (b[j] - g_mod[j-1]*a[j])
        g_mod.append(gg)
    '''Calculate d_mod[]'''
    d_mod = [d[0] / b[0]]
    for j in range(1,n):
        dd = (d[j] - d_mod[j-1]*a[j]) / (b[j] - g_mod[j-1]*a[j])
        d_mod.append(dd)
    '''Calculate x'''
    x[n-1] = d_mod[-1]  
    for j in range(n-2,-1,-1):
        x[j] = d_mod[j] - g_mod[j]*x[j+1]
    return x
