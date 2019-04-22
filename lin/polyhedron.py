import numpy as np
import itertools as it
from math import factorial
import re


def permutation(m, n):
    return factorial(n) / (factorial(n - m) * factorial(m))


def matrix_combinations(matr, n):
    timed = list(map(list, it.combinations(matr, n)))
    return np.array(list(timed))


def array_combinations(arr, n):
    timed = list(map(list, it.combinations(arr, n)))
    return np.array(list(timed))


def check_extreme(matr, arr, x, sym_comb, m):
    sym_comb = sym_comb.replace(']', '')
    sym_comb = sym_comb.replace('[', '')
    sym_comb = re.split("[ ,]", sym_comb)
    for i in range(int(m)):
        td_answer = sum(matr[i] * x)
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


def extreme_points(A, b, sym_comb):
    # Input
    A = np.array(A)
    b = np.array(b)
    m, n = A.shape
    # Process
    ans_comb = np.zeros((1, n))
    arr_comb = array_combinations(b, n)
    matr_comb = matrix_combinations(A, n)
    for i in range(int(permutation(n, m))):
        if np.linalg.det(matr_comb[i]) != 0:
            x = np.linalg.solve(np.array(matr_comb[i], dtype='float'),
                                np.array(arr_comb[i], dtype='float'))
            ans_comb = np.vstack([ans_comb, x])
    ans_comb = np.delete(ans_comb, 0, axis=0)
    j = 0
    for i in range(len(ans_comb)):
        if check_extreme(A, b, ans_comb[j], sym_comb, m):
            ans_comb = ans_comb
            j += 1
        else:
            ans_comb = np.delete(ans_comb, j, axis=0)
    # Output
    return ans_comb
