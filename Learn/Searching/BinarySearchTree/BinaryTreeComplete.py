class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    @staticmethod
    def tuple_to_tree(data):
        if data is None:
            return None
        elif isinstance(data, tuple) and len(data) == 3:
            node = BinaryTree(data[1])
            node.left = BinaryTree.tuple_to_tree(data[0])
            node.right = BinaryTree.tuple_to_tree(data[2])
        else:
            node = BinaryTree(data)
        return node

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return (
            self.left.to_tuple() if self.left else None,
            self.key,
            self.right.to_tuple() if self.right else None,
        )

    def display_keys(self, space="\t", level=0):
        if self is None:
            print(space * level + "*")
            return
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
        BinaryTree.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        BinaryTree.display_keys(self.left, space, level + 1)

    def height(self):
        if self is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def node(self):
        if self is None:
            return 0
        left_node = self.left.node() if self.left else 0
        right_node = self.right.node() if self.right else 0
        return 1 + left_node + right_node

    def traverse_inorder(self):
        if self is None:
            return []
        left_keys = self.left.traverse_inorder() if self.left else []
        right_keys = self.right.traverse_inorder() if self.right else []
        return left_keys + [self.key] + right_keys

    def __str__(self) -> str:
        return f"BinaryTree <{self.to_tuple()}>"

    def __repr__(self) -> str:
        return self.__str__()


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = BinaryTree.tuple_to_tree(tree_tuple)
tree.display_keys()
tree.height()
tree.node()
tree.traverse_inorder()
tree.to_tuple()
