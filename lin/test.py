import numpy as np
from .polyhedron import extreme_points


def test():
    A = [[1,  0, 0],
         [1, -1, 1],
         [1, -2, 0],
         [0,  1, 0],
         [0,  0, 1]]
    b = [0, 1, 4, 0, 0]
    c = '[>=,<=,<=,>=,>=]'
    expected = [[0, 0, 1],
                [0, 0, 0],
                [1, 0, 0]]
    ans = extreme_points(A, b, c)
    assert np.allclose(ans, expected, atol=1e-12, rtol=0)
