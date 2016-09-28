import math


def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def minkovski_distance(a, b, n):
    return math.pow(math.pow(a[0] - b[0], n) + math.pow(a[1] - b[1], n), 1/n)

