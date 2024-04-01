"""
Floyd's Cycle Finding Algorithm, also known as the Tortoise and Hare Algorithm
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(nodes: Node) -> bool:
    slow = nodes
    fast = nodes

    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast and slow.val == fast.val:
            return True

    return False
