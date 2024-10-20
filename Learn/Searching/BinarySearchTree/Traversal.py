"""
Inorder   : Left , Root, Right
Preorder  : Root, Left , Right
Postorder : Left , Right , Root

"""
# Binary Search


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(tree_tuple)


def display_tree(node, space="\t", level=0):
    if node is None:
        print(space * level + "∅")
        return
    if node.left is None and node.right is None:
        print(space * level + str(node.data))
        return
    display_tree(node.right, space, level + 1)
    print(space * level + str(node.data))
    display_tree(node.left, space, level + 1)


display_tree(tree2)


# Inorder Traversal :
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


inorder(tree2)


# Postorder Traversal :
def postorder(node):
    if node is None:
        return []
    return [node.data] + postorder(node.left) + postorder(node.right)


postorder(tree2)


# Preorder Traversal :
def preorder(node):
    if node is None:
        return []
    return preorder(node.left) + preorder(node.right) + [node.data]


preorder(tree2)
