from collections import deque
from typing import List


def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    def get_neighbor(node: str) -> List[str]:
        result = []
        for word in word_list:
            count_diff = 0
            if len(begin) == len(word):
                for idx, ch in enumerate(node):
                    if word[idx] != ch:
                        count_diff += 1
                if count_diff == 1:
                    result.append(word)

        return result

    def bfs(node):
        count_step = 0
        queue = deque([node])
        visited = set([node])

        while len(queue):
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                for neighbor in get_neighbor(curr):
                    if neighbor in visited:
                        continue
                    if neighbor == end:
                        count_step += 1
                        return count_step
                    queue.append(neighbor)
                    visited.add(neighbor)
            count_step += 1

        return count_step

    print(bfs(begin))
    return 0


if __name__ == "__main__":
    begin = "COLD"
    end = "WARM"
    word_list = ["COLD", "CORD", "CARD", "WARD", "WARM", "TARD"]
    res = word_ladder(begin, end, word_list)
    print(res)
