from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists1(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """use array and sort then put back into listnode"""
        temp_list = []
        while list1:
            temp_list.append(list1.val)
            list1 = list1.next
        while list2:
            temp_list.append(list2.val)
            list2 = list2.next
        temp_list = sorted(temp_list)
        # use two object for iterating
        result_listnode = dummy = ListNode(temp_list.pop(0))
        for number in temp_list:
            current = ListNode(number)
            dummy.next = current
            dummy = dummy.next

        return result_listnode

    def mergeTwoLists2(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2

        return head.next


def print_listnode(list_node):
    result = []
    while list_node:
        result.append(list_node.val)
        list_node = list_node.next
    print(result)


if __name__ == "__main__":
    list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(4)))
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(4)))
    # list_node = Solution().mergeTwoLists1(list1=list1, list2=list2)
    list_node = Solution().mergeTwoLists2(list1=list1, list2=list2)

    print_listnode(list_node=list_node)
