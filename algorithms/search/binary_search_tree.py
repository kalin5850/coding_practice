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

    def breadth_first_search(self):
        "use queue for implementing BFS"
        queue = []
        result = []
        current_node = self.root
        queue.insert(0, current_node)
        while len(queue) > 0:
            current_node = queue.pop()
            result.append(current_node.data)
            if current_node.left:
                queue.insert(0, current_node.left)
            if current_node.right:
                queue.insert(0, current_node.right)

        return result

    def breadth_frist_search_rescursive(self, queue, result):
        # base case
        if len(queue) < 1:
            return result
        current_node = queue.pop()
        result.append(current_node.data)
        if current_node.left:
            queue.insert(0, current_node.left)
        if current_node.right:
            queue.insert(0, current_node.right)

        return self.breadth_frist_search_rescursive(queue=queue, result=result)

    def DFSInorder(self):
        def traverse_inorder(node, result):
            # base case
            if not node:
                return result
            if node.left:
                traverse_inorder(node.left, result)
            result.append(node.data)
            if node.right:
                traverse_inorder(node.right, result)

            return result

        result = traverse_inorder(node=self.root, result=[])
        print("Traverse Inorder: %s" % (result,))

    def DFSPreorder(self):
        def traverse_preorder(node, result):
            # base case
            if not node:
                return result
            result.append(node.data)
            if node.left:
                traverse_preorder(node=node.left, result=result)
            if node.right:
                traverse_preorder(node=node.right, result=result)

            return result

        result = traverse_preorder(node=self.root, result=[])
        print("Traverse Preorder: %s" % (result,))

    def DFSPostorder(self):
        def traverse_postorder(node, result):
            # base case
            if not node:
                return result
            if node.left:
                traverse_postorder(node=node.left, result=result)
            if node.right:
                traverse_postorder(node=node.right, result=result)

            result.append(node.data)
            return result

        result = traverse_postorder(node=self.root, result=[])
        print("Traverse Postorder: %s" % (result))


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(9)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(20)
    binary_tree.insert(170)
    binary_tree.insert(15)
    binary_tree.insert(1)

    # print(binary_tree.search(value=1))
    # print(binary_tree)
    print(binary_tree.breadth_first_search())
    # print(
    #     binary_tree.breadth_frist_search_rescursive(
    #         queue=[binary_tree.root], result=[]
    #     )
    # )
    # binary_tree.DFSInorder()
    # binary_tree.DFSPreorder()
    # binary_tree.DFSPostorder()

##      9
##   4     20
## 1  6  15  170
# Inorder 1, 4, 6, 9, 15, 20, 170
# Preorder 9, 4, 1, 6, 20, 15, 170
# Postorder 1, 6, 4, 15, 170, 20, 9

"""
If a graph has weight value, use Bellman or Dijkstra
    
    use Bellman when the weight has negative, worst case is N^2
    
    use Dijkstra when the weights are positive

"""
