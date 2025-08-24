import sys
from math import sqrt


def closest_pair(points):
    closest = None
    min_dist = sys.float_info.max
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            dist = calc_dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest = (points[i], points[j])
    return closest


def calc_dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


if __name__ == '__main__':
    points = (
        (2, 2),  # A
        (2, 8),  # B
        (5, 5),  # C
        (6, 3),  # D
        (6, 7),  # E
        (7, 4),  # F
        (7, 9)  # G
    )
    print(closest_pair(points)) #((6, 3), (7, 4))