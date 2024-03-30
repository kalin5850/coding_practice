"""
You are faced with a 4-wheel lock where each wheel contains the numbers '0' through '9'. Turning a wheel can either increase or decrease its number by one, wrapping around from '9' to '0' or vice versa. A single move involves rotating any one of the wheels by one slot.

The lock starts with the combination '0000'. However, there are specific combinations termed as "deadends". If the lock lands on any of these deadend combinations, the wheels jam, making it impossible to proceed.

Your task is to determine the least number of moves needed to reach a given target combination from the starting point without hitting any deadend. If reaching the target is impossible due to deadends, return -1.

Input

target_combo: a string representing the four digit combination to open the lock.
trapped_combos: a list of strings representing the trapped combinations.
Output

An integer representing the number of steps it takes to open the lock, or -1 if you can't open it without triggering the trap.

Examples

Example 1:

Input:

target_combo = "0202"
trapped_combos = ["0201","0101","0102","1212","2002"]
Output: 6

Explanation:

0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202, a total of 6 steps.

Constraints

The starting combination (0000) and the final combination is not trapped because that defeats the purpose of the lock.
"""

from collections import deque
from typing import List


def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    def get_neighbors(node: str) -> List[str]:
        result = []
        node = list(node)
        for idx, value in enumerate(node):
            tmp = node[:]
            # increase
            tmp[idx] = str((int(value) + 1) % 10)
            result.append("".join(tmp))
            # decrease
            tmp[idx] = str((int(value) - 1 + 10) % 10)
            result.append("".join(tmp))

        return result

    def bfs(node: str) -> int:
        queue = deque([node])
        visited = set(trapped_combos[:])
        visited.add(node)
        count = 0

        while len(queue):
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                for neighbor in get_neighbors(curr):
                    if neighbor in visited:
                        continue
                    if neighbor == target_combo:
                        count += 1
                        return count
                    queue.append(neighbor)
                    visited.add(neighbor)
            count += 1

        return -1

    return bfs("0000")
