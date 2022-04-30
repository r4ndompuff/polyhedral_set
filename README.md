# Brief description
This is a program for finding extreme points of polyhedral set. //
Программа для поиска крайних точек канонического многогранника.

# Used libraries
numpy, itertools, math, re

# How to install

    pip install lin

or

    pip install git+https://github.com/r4ndompuff/polyhedral_set

# Input type

    extreme_points(A, b, c)
    
Where

* A - m×n matrix of coefficients
* b - 1×m row vector of free coefficients on the right side
* c - string of inequality (or equality) signs

# How to use it

    import lin.polyhedron as ph

Example:

    A = [[1,  0, 0],
         [1, -1, 1],
         [1, -2, 0],
         [0,  1, 0],
         [0,  0, 1]]
    b = [0, 1, 4, 0, 0]
    c = '[>=,<=,<=,>=,>=]'
    ans = ph.extreme_points(A, b, c)
    print(ans)

# Description / Описание

Getting extreme points for polyhedral set H = {x in R^n: w^(T)x>=-b} and other 
types such as U = {u in R^n|Au=b, u>=0}

Поиск всех крайних точек канонического многогранника H = {x in R^n: w^(T)x+b>=0} 
и всех его частных случаев U = {u in R^n|Au=b, u>=0}

# Typical errors

1) If you have `ImportError: No module named polyhedron`. Then use 
   `polyhedron` instead of `lin.polyhedron` in import.
2) If you have any more problems, open an Issue here.
