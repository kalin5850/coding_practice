class Stack:
    def __init__(self):
        self.stack_list = []

    def peek(self):
        return self.stack_list[len(self.stack_list) - 1]

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        remove_node = self.stack_list.pop()
        return remove_node

    def is_empty(self):
        return len(self.stack_list) == 0

    def print_stack(self):
        print(self.stack_list)


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
