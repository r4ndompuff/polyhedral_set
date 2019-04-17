# Brief description
This is a program for finding extreme points of polyhedral set. // Программа для поиска крайних точек канонического многогранника.

# Used libraries
numpy, itertools, math, re

# Input type
extreme_points(m,n,A,b,c) <br/>
Where m - integer of how many raws in A (and b) <br/>
n - integer of how many x's (columns) in A <br/>
A - it is a matrix of coefficients <br/>
b - it is a vector of free coefficients on the right side (check Description)<br/>
c - it is a string (!!!) of inequality (or equality) signs 

# How to use it
Example 1: print(ph.extreme_points(5,3,[[1,0,0],[1,-1,1],[1,-2,0],[0,1,0],[0,0,1]],[0,1,4,0,0],'[>=,<=,<=,>=,>=]')) <br/>
Example 2: A = [[1,0,0],[1,-1,1],[1,-2,0],[0,1,0],[0,0,1]] <br/>
b = [0,1,4,0,0] <br/>
c = '[>=,<=,<=,>=,>=]' <br/>
ans = extreme_points(5,3,A,b,c)

# Description/Описание
Getting extreme points for polyhedral set H = {x in R^n: w^(T)x>=-b} and other types such as U = {u in R^n|Au=b, u>=0} <br/>
Поиск всех крайних точек канонического многогранника H = {x in R^n: w^(T)x+b>=0} и всех его частных случаев U = {u in R^n|Au=b, u>=0}