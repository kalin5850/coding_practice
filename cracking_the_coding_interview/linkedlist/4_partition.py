# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition1(self, linkedlist: ListNode, x: int) -> ListNode:
        "two pointers"
        left_linkedlist = left_tmp = None
        right_linkedlist = right_tmp = None
        current_node = linkedlist
        while current_node != None:
            if current_node.val < x and left_tmp == None:
                left_tmp = current_node
                left_linkedlist = left_tmp
            elif current_node.val < x and left_tmp != None:
                left_tmp.next = current_node
                left_tmp = left_tmp.next
            elif current_node.val >= x and right_tmp == None:
                right_tmp = current_node
                right_linkedlist = right_tmp
            elif current_node.val >= x and right_tmp != None:
                right_tmp.next = current_node
                right_tmp = right_tmp.next
            current_node = current_node.next

        current_node = left_linkedlist
        while True:
            if current_node.next == None:
                current_node.next = right_linkedlist
                break
            current_node = current_node.next

        return left_linkedlist

    def print_list(self, linkedlist: ListNode):
        current_node = linkedlist
        result = []
        while current_node != None:
            result.append(current_node.val)
            current_node = current_node.next
        return result


if __name__ == "__main__":
    # 3 -> 5 -> 8 -> 5 -> 10 -> 12 -> 3 -> 5
    list1 = ListNode(
        val=3,
        next=ListNode(
            val=5,
            next=ListNode(
                val=8,
                next=ListNode(
                    val=5,
                    next=ListNode(
                        val=10,
                        next=ListNode(
                            val=12, next=ListNode(val=3, next=ListNode(val=5))
                        ),
                    ),
                ),
            ),
        ),
    )
    result = Solution().partition1(list1, 5)
    print(Solution().print_list(result))
