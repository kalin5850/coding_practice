class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self, data):
        new_node = Node(data=data)
        if self.top is None:
            self.bottom = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        remove_node = self.top
        self.top = self.top.next
        self.length -= 1
        return remove_node.data

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        result_stack = []
        current_node = self.top
        while current_node:
            result_stack.append(current_node.data)
            current_node = current_node.next
        print(result_stack)


if __name__ == "__main__":
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push("google")
    my_stack.push("Udemy")
    my_stack.push("Discord")
    my_stack.print_stack()
    print(my_stack.is_empty())
    print(my_stack.peek())
    my_stack.push("linkedin")
    my_stack.print_stack()
    print(my_stack.peek())
    print("pop stack %s" % (my_stack.pop(),))
    my_stack.print_stack()
