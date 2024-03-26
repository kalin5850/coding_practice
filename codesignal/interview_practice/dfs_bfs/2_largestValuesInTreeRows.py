"""
You have a binary tree t. Your task is to find the largest value in each row of this tree. In a tree, a row is a set of nodes that have equal depth. For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

Return an array in which the first element is the largest value in the row with depth 0, the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.

Example

For

t = {
    "value": -1,
    "left": {
        "value": 5,
        "left": null,
        "right": null
    },
    "right": {
        "value": 7,
        "left": null,
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = [-1, 7, 1].

The tree in the example looks like this:

    -1
   / \
  5   7
       \
        1
In the row with depth 0, there is only one vertex - the root with value -1;
In the row with depth 1, there are two vertices with values 5 and 7, so the largest value here is 7;
In the row with depth 2, there is only one vertex with value 1.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 5 · 104,
-1000 ≤ node value ≤ 1000.

[output] array.integer

An array of the largest values in each row of t.
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import deque

def solution(t):
    
    def bfs(node):
        queue = deque([node])
        result = []
        
        if not node:
            return result
        
        while len(queue):
            n = len(queue)
            tmp = []
            for _ in range(n):
                curr = queue.popleft()
                tmp.append(curr.value)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(max(tmp))
        
        return result
    
    return bfs(t)
                

