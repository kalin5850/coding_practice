from typing import List


def generate_parentheses(n: int) -> List[str]:
    result = []

    def dfs(idx, path, open_counter, close_counter):
        if idx == n * 2:
            result.append("".join(path))
            return

        for parenthesis in ["(", ")"]:
            # prune branches
            if parenthesis == "(" and open_counter >= n:
                continue
            if parenthesis == ")" and close_counter >= open_counter:
                continue

            path.append(parenthesis)
            if parenthesis == "(":
                open_counter += 1
            if parenthesis == ")":
                close_counter += 1

            dfs(idx + 1, path, open_counter, close_counter)

            # backtracking
            if parenthesis == "(":
                open_counter -= 1
            if parenthesis == ")":
                close_counter -= 1
            path.pop()

    dfs(0, [], 0, 0)

    return result


if __name__ == "__main__":
    # n = int(input())
    n = 2
    res = generate_parentheses(n)
    for line in sorted(res):
        print(line)
