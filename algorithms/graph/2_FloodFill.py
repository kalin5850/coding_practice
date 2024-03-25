"""
In computer graphics, an uncompressed raster image is presented as a matrix of numbers. Each entry of the matrix represents the color of a pixel. A flood fill algorithm takes a coordinate r, c and a replacement color, and replaces all pixels connected to r, c that have the same color (i.e., the pixels connected to the given coordinate with same color and all the other pixels connected to the those pixels of the same color) with the replacement color. (e.g. MS-Paint's paint bucket tool).

Input

r: row
c: column
replacement: replacement color
image: an 2D array of integers representing the image
Output

the replaced image

Examples

Example 1:

Input:

1r = 2
2c = 2
3replacement = 9
4arr = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
Output: [[0,1,3,4,1],[3,9,9,3,3],[6,7,9,9,3],[12,2,9,9,1],[12,3,1,3,2]]

Explanation:

From

0 1 3 4 1
3 8 8 3 3
6 7 8 8 3
12 2 8 9 1
12 3 1 3 2

to

0 1 3 4 1
3 9 9 3 3
6 7 9 9 3
12 2 9 9 1
12 3 1 3 2
"""

from collections import deque
from typing import List, Set


def floodFile(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    
    start_color = image[r][c]
    
    def dfs(r, c):
        if (
            r < 0 or r > len(image) - 1 or 
            c < 0 or c > len(image[0]) - 1 or 
            image[r][c] != start_color
        ):
            return
        
        image[r][c] = replacement
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
           
    dfs(r, c)
    return image

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])
    
    def get_neighbors(coord, color: int):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
                                         
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                   yield neighbor_row, neighbor_col
    
    def bfs(r: int, c: int) -> None:
        queue = deque([(r, c)])
        visited = set([(r, c)])
        color = image[r][c]
        image[r][c] = replacement
        
        while len(queue):
            curr = queue.popleft()
            for neighbor in get_neighbors(curr, color):
                r, c = neighbor
                if neighbor in visited:
                    continue
                image[r][c] = replacement
                queue.append(neighbor)
                visited.add(neighbor)
                
    bfs(r, c)    
    return image

if __name__ == '__main__':
    # r = int(input())
    # c = int(input())
    # replacement = int(input())
    # image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    r = 2
    c = 2
    replacement = 9
    image = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
    # res = flood_fill(r, c, replacement, image)
    # for row in res:
    #     print(' '.join(map(str, row)))
    
    res = floodFile(r, c, replacement, image)
    for row in res:
        print(' '.join(map(str, row)))
