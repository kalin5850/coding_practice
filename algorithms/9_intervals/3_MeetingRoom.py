"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings.

Example: 1

Input:

intervals = [[0,30],[5,10],[15,20]]
Output:

false
Example: 2

Input:

intervals = [[7,10],[2,4]]
Output:

true
"""

from typing import List


def meeting_rooms(intervals: List[List[int]]) -> bool:
    intervals.sort()
    result = []

    for interval in intervals:
        if len(result) == 0:
            result.append(interval)
        elif result[-1][1] < interval[1]:
            result.append(interval)
        else:
            return False

    return True
