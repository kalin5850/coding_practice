"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
solution(grid) = true;
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
solution(grid) = false.

"""


def get_subs(grid):
    subs = []
    for i in range(0, len(grid), 3):
        for j in range(0, len(grid), 3):
            tmp = []
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    tmp.append(grid[k][l])
            subs.append(tmp)
    return subs


def is_valid(arr):
    digits = []
    for ch in arr:
        if ch.isdigit():
            digits.append(ch)

    return len(digits) == len(set(digits))


if __name__ == "__main__":
    grid = [
        [".", ".", ".", "1", "4", ".", ".", "2", "."],
        [".", ".", "6", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "1", ".", ".", ".", ".", ".", "."],
        [".", "6", "7", ".", ".", ".", ".", ".", "9"],
        [".", ".", ".", ".", ".", ".", "8", "1", "."],
        [".", "3", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", "7", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", "7", "."],
    ]

    rows = grid
    cols = zip(*grid)
    subs = get_subs(grid)
    # print(all(list(map(is_valid, rows))))
    # print(all(list(map(is_valid, list(cols)))))
    print(
        all(
            [
                all(list(map(is_valid, rows))),
                all(list(map(is_valid, list(cols)))),
                all(list(map(is_valid, subs))),
            ]
        )
    )
