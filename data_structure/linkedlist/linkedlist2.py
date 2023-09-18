# 10 --> 5 --> 16


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        head_node = Node(value)
        head_node.next = self.head
        self.head = head_node
        self.length += 1

    def insert(self, position, value):
        if position == 1:
            self.prepend(value)
            return
        if position == self.length + 1:
            self.append(value)
            return
        new_node = Node(value)
        index = position - 1
        while index == 0:
            self.head = self.head.next
            index -= 1
        tmp_node = self.head.next
        self.head.next = new_node
        new_node.next = tmp_node
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            while index != 1:
                current_node = current_node.next
                index -= 1
            remove_node = current_node.next
            current_node.next = remove_node.next
            self.length -= 1

    def reverse(self):
        first_node = self.head
        second_node = self.head.next
        self.tail = self.head
        while second_node:
            tmp = second_node.next
            second_node.next = first_node
            first_node = second_node
            second_node = tmp
        self.head = first_node
        self.tail.next = None

    def print_list(self):
        current_node = self.head
        result = []
        while current_node != None:
            result.append(current_node.value)
            current_node = current_node.next
        return result


if __name__ == "__main__":
    linked_list = LinkedList(10)
    linked_list.append(5)
    linked_list.append(16)
    linked_list.append(1)
    linked_list.prepend(20)
    linked_list.insert(2, 99)
    linked_list.insert(1, 199)
    linked_list.insert(8, 299)
    print(linked_list.print_list())
    linked_list.remove(3)
    print(linked_list.print_list())
    print(linked_list.length)
    linked_list.reverse()
    print(linked_list.print_list())
