# Darts
import math


def darts(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)
    if dist > 10:
        return 0
    elif 5 <= dist <= 10:
        return 1
    elif 1 <= dist <= 5:
        return 5
    elif 0 <= dist <= 1:
        return 10
