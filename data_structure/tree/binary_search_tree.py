class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, value):
        new_node = Node(data=value)
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
        else:
            current_node = self.root
            while True:
                if (
                    new_node.data < current_node.data
                    and current_node.left is not None
                ):
                    current_node = current_node.left
                elif (
                    new_node.data >= current_node.data
                    and current_node.right is not None
                ):
                    current_node = current_node.right
                elif (
                    new_node.data < current_node.data
                    and current_node.left is None
                ):
                    current_node.left = new_node
                    self.number_of_nodes += 1
                    break
                elif (
                    new_node.data >= current_node.data
                    and current_node.right is None
                ):
                    current_node.right = new_node
                    self.number_of_nodes += 1
                    break

    def search(self, value):
        if self.root is None:
            return "Tree is empty"
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return "Not Found"
                if value == current_node.data:
                    return "Found value"
                elif value < current_node.data:
                    current_node = current_node.left
                elif value > current_node.right:
                    current_node = current_node.right

    def remove(self, value):
        pass


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(9)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(20)
    binary_tree.insert(170)
    binary_tree.insert(15)
    binary_tree.insert(1)

    print(binary_tree.search(value=1))

    print(binary_tree)
