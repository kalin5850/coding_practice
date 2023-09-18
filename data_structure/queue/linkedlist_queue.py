class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.top.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        remove_node = self.first
        self.first = self.first.next
        self.length -= 1
        return remove_node.data

    def is_empty(self):
        return self.first is None

    def print_queue(self):
        result = []
        current_node = self.first
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        print(result)


if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue("This")
    my_queue.enqueue("is")
    my_queue.enqueue("a")
    my_queue.enqueue("Queue")
    my_queue.print_queue()
    my_queue.dequeue()
    my_queue.print_queue()
