# Tridiagonal-Matrix-Solver-via-Thomas-Algorithm-in-Python
Tridiagonal-Matrix-Solver-via-Thomas-Algorithm-in-Python

Thomas-Algorithm refer to wiki: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
Here x in A x = d is solved.
the meaning of a b c in thomaxsolver.py is the same as those in wiki, that is 
  In A matrix:
    a is lower diagonal;
    b is main diagonal;
    c is upper diagonal.
Note that: a b c have the same dimension and they are all zero-based in python, 
           so the terms a[0]=0 and c[-1]=0 should be added in a and c in order to 
           keep the same dimension with b and it is just for the convenience in calculation 
           without having any effect on the result.
If you have a tridiagonal matrix A which is difficult to get a b c, you can solve it with 
Python built-ins 'from scipy.linalg import solve_banded'.
