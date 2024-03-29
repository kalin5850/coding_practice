""""""

from typing import List


def solution(inputString: str) -> str:
    stack = []

    for ch in inputString:
        if ch == ")":
            reverse = []
            while True:
                tmp = stack.pop()
                if tmp == "(":
                    break
                else:
                    reverse.append(tmp)
            stack += reverse
        else:
            stack.append(ch)

    return "".join(stack)


if __name__ == "__main__":
    inputString = "foo(bar(baz))blim"
    solution(inputString)
