def solution(n, k):
    result = []

    def dfs(idx, path, state):
        if state == n:
            # print(path)
            result.append(path[:])
            return

        for i in range(idx, k + 1):
            state += i
            if state <= n:
                path.append(i)
                dfs(idx, path, state)
                state -= path.pop()

        return

    dfs(1, [], 0)

    return result


print(solution(4, 2))
