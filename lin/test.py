from .polyhedron import extreme_points


def test():
    A = [[1,  0, 0],
         [1, -1, 1],
         [1, -2, 0],
         [0,  1, 0],
         [0,  0, 1]]
    b = [0, 1, 4, 0, 0]
    c = '[>=,<=,<=,>=,>=]'
    print(extreme_points(5, 3, A, b, c))
