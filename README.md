# Brief description
This is a program for finding extreme points of polyhedral set. // Программа для поиска крайних точек канонического многогранника.

# Used libraries
numpy (ver. 1.15.4), itertools, math, re

# How to install
pip install lin <br/>
    or    <br/>
pip install git+https://github.com/r4ndompuff/polyhedral_set

# Input type
extreme_points(m,n,A,b,c) <br/>
Where m - integer of how many raws in A (and b) <br/>
n - integer of how many x's (columns) in A <br/>
A - it is a matrix of coefficients <br/>
b - it is a vector of free coefficients on the right side (check Description)<br/>
c - it is a string (!!!) of inequality (or equality) signs 

# How to use it
import polyhedron as ph <br/>
Example 1: print(ph.extreme_points(5,3,[[1,0,0],[1,-1,1],[1,-2,0],[0,1,0],[0,0,1]],[0,1,4,0,0],'[>=,<=,<=,>=,>=]')) <br/>
Example 2: A = [[1,0,0],[1,-1,1],[1,-2,0],[0,1,0],[0,0,1]] <br/>
b = [0,1,4,0,0] <br/>
c = '[>=,<=,<=,>=,>=]' <br/>
ans = extreme_points(5,3,A,b,c)

# Description
Getting extreme points for polyhedral set H = {x in R^n: w^(T)x>=-b} and other types such as U = {u in R^n|Au=b, u>=0} <br/>
Поиск всех крайних точек канонического многогранника H = {x in R^n: w^(T)x+b>=0} и всех его частных случаев U = {u in R^n|Au=b, u>=0}

# Typical errors
1) If you use python3, then try to use python 2.7. <br/>
2) If you want to you use python 3, then if you have numpy error, then download in manually (or use python 2.7 instead). <br/>
3) If you have "ImportError: No module named polyhedron". Then use 'lin.polyhedron' instead of 'polyhedron' in import. (This is because you use python 3 or install python 3, when you already had the best python 2.7)
4) If you have any more problems. Contact me: r4nd0m1999@gmail.com.
