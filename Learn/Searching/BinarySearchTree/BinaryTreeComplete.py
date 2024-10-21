class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    @staticmethod
    def tuple_tree(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = BinaryTree(data[1])
            node.left = BinaryTree.tuple_tree(data[0])
            node.right = BinaryTree.tuple_tree(data[2])
        else:
            node = BinaryTree(data)
        return node

    def display_tree(self, space="\t", level=0):
        if self is None:
            print(space * level + "*")
            return

        if self.right:
            self.right.display_tree(space, level + 1)
        else:
            print((space * (level + 1)) + "*")

        print(space * (level) + str(self.key))

        if self.left:
            self.left.display_tree(space, level + 1)
        else:
            print((space * (level + 1)) + "*")


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = BinaryTree.tuple_tree(tree_tuple)
tree
tree.left.key
tree.display_tree()
tree.traverse_inorder()
