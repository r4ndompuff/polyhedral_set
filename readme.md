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

    extreme_points(m,n,A,b,c)
    
Where

* m - integer of how many raws in A (and b)
* n - integer of how many x's (columns) in A
* A - matrix of coefficients
* b - vector of free coefficients on the right side (check 
  Description)
* c - string of inequality (or equality) signs 

# How to use it

    import polyhedron as ph

Example:

    A = [[1,0,0],[1,-1,1],[1,-2,0],[0,1,0],[0,0,1]]
    b = [0,1,4,0,0]
    c = '[>=,<=,<=,>=,>=]'
    ans = ph.extreme_points(5,3,A,b,c)
    print(ans)

# Description / Описание

Getting extreme points for polyhedral set H = {x in R^n: w^(T)x>=-b} and other 
types such as U = {u in R^n|Au=b, u>=0}

Поиск всех крайних точек канонического многогранника H = {x in R^n: w^(T)x+b>=0} 
и всех его частных случаев U = {u in R^n|Au=b, u>=0}

# Typical errors

1) If you use python3, then try to use python 2.7.
2) If you want to you use python 3, then if you have numpy error, then download 
   in manually (or use python 2.7 instead).
3) If you have "ImportError: No module named polyhedron". Then use 
   `lin.polyhedron` instead of `polyhedron` in import. (This is because you use 
   python 3 or installed python 3, when you already had the best python 2.7)
4) If you have any more problems. Contact me: r4nd0m1999@gmail.com.
