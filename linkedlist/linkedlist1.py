# 10 --> 5 --> 16


class LinkedList:
    def __init__(self, value) -> None:
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        head_node = {"value": value, "next": None}
        head_node["next"] = self.head
        self.head = head_node
        self.length += 1


if __name__ == "__main__":
    linked_list = LinkedList(10)
    linked_list.append(5)
    linked_list.append(16)
    linked_list.append(1)
    linked_list.prepend(20)
    print(linked_list)
