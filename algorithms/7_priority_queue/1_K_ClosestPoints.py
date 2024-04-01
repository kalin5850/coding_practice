"""
Given a list of points on a 2D plane. Find k closest points to the origin (0, 0).

Input: [(1, 1), (2, 2), (3, 3)], 1

Output: [(1, 1)]
"""

import heapq
from typing import List


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    distant = []
    result = []
    for point in points:
        distant_twice = pow(point[0] - 0, 2) + pow(point[1] - 0, 2)
        heapq.heappush(distant, (distant_twice, point))

    for _ in range(k):
        result.append(heapq.heappop(distant)[1])

    return result
