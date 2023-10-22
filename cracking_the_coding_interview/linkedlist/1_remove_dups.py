# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_dups(self, linkedlist: ListNode) -> ListNode:
        """
        Brute Force, time complexity is O(n) and space complexity is O(n)
        """
        current_node = linkedlist
        previous_node = linkedlist
        values_list = []
        while current_node != None:
            if current_node.val not in values_list:
                values_list.append(current_node.val)
                previous_node = current_node
                current_node = current_node.next
            else:
                previous_node.next = current_node.next
                current_node = current_node.next

    def print_list(self, linkedlist):
        current_node = linkedlist
        result = []
        while current_node != None:
            result.append(current_node.val)
            current_node = current_node.next
        return result


if __name__ == "__main__":
    # 7 -> 3 -> 4 -> 5 -> 4
    list1 = ListNode(
        val=7,
        next=ListNode(
            val=3, next=ListNode(4, next=ListNode(val=5, next=ListNode(4)))
        ),
    )
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(4)))

    Solution().remove_dups(linkedlist=list1)
    print(Solution().print_list(linkedlist=list1))
