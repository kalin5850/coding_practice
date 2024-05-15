"""
Given a collection of intervals, merge all overlapping intervals.

Example: 1

Input:

intervals = [[1,3],[2,6],[8,10],[15,18]]
Output:

[[1,6],[8,10],[15,18]]
Explanation:

Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].

Example: 2

Input:

intervals = [[1,4],[4,5]]
Output:

[[1,5]]
Explanation:

Intervals [1,4] and [4,5] are considered to be overlapping.

Constraints:


"""

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result = []
    for interval in intervals:
        if len(result) == 0:
            result.append(interval)
        # not overlapping
        elif result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = merge_intervals(intervals)
    for row in res:
        print(" ".join(map(str, row)))
    intervals = [[1, 4], [4, 5]]
    res = merge_intervals(intervals)
    for row in res:
        print(" ".join(map(str, row)))
