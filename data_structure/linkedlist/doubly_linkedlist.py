class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.index = 0
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        self.tail = new_node
        current_node.next = new_node
        new_node.prev = current_node
        self.length += 1
        self.index += 1

    def print_list(self):
        result = []
        current_node = self.head
        while current_node != None:
            result.append(current_node.value)
            current_node = current_node.next

        return result


if __name__ == "__main__":
    my_doubly_linkedlist = DoublyLinkedList(10)
    my_doubly_linkedlist.append(20)
    my_doubly_linkedlist.append(30)
    my_doubly_linkedlist.append(40)
    print(my_doubly_linkedlist.print_list())
