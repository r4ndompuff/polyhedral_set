import numpy as np
import itertools as it
import math
import re

def permutation(m,n):
	return math.factorial(n)/(math.factorial(n-m)*math.factorial(m))

def matrix_combinations(matr,n):
	timed = list(map(list, it.combinations(matr, n)))
	for i in range(n):
		timed[i][i][i] = np.asscalar(timed[i][i][i])
	all = np.array(list(timed))
	return all

def array_combinations(arr,n):
	timed = list(map(list, it.combinations(arr, n)))
	for i in range(n):
		timed[i][i] = np.asscalar(timed[i][i])
	all = np.array(list(timed))
	return all

def check_extreme(matr, arr, x, sym_comb, m):
	sym_comb = sym_comb.replace(']', '')
	sym_comb = sym_comb.replace('[', '')
	sym_comb = re.split("[ ,]", sym_comb)
	for i in range(m):
		td_answer = sum(matr[i]*x)
		if sym_comb[i] == '>':
			if td_answer <= arr[i]:
				return 0
		elif sym_comb[i] == '>=':
			if td_answer < arr[i]:
				return 0
		elif sym_comb[i] == '<':
			if td_answer >= arr[i]:
				return 0
		elif sym_comb[i] == '<=':
			if td_answer > arr[i]:
				return 0
		elif sym_comb[i] == '=':
			if td_answer != arr[i]:
				return 0
		elif sym_comb[i] == '!=':
			if td_answer == arr[i]:
				return 0
		else:
			return 0
	return 1

def extreme_points(m,n,A,b,sym_comb):
	# Input
	A = np.array(A).reshape(m,n)
	b = np.array(b).reshape(m,1)
	# Proccess
	ans_comb = np.zeros((1,n))
	arr_comb = array_combinations(b,n)
	matr_comb = matrix_combinations(A,n)
	for i in range(int(permutation(n,m))):
		if np.linalg.det(matr_comb[i]) != 0:
			x = np.linalg.solve(matr_comb[i],arr_comb[i])
			ans_comb = np.vstack([ans_comb,x])
	ans_comb = np.delete(ans_comb, (0), axis=0)
	j = 0
	for i in range(len(ans_comb)):
		if check_extreme(A, b, ans_comb[j], sym_comb, m):
			ans_comb = ans_comb
			j = j + 1
		else:
			ans_comb = np.delete(ans_comb, (j), axis=0)
	# Output
	return ans_comb