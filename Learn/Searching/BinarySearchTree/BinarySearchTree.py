"""
Binary Tree : Each node can contain atmost 2 nodes [0,1,2]

Binary Search Tree :
    => If the Binary Tree is arranged in a way such that
        * the left node is always smaller than the middle node and
        * the right node is always larger than the middle node
        * in the lexicographical order.
    => The node contains key and those keys (Username) are mapped with values (user)

Balanced Search Tree:
    => If the above tree is balanced such that not right or left skewed
        * Difference can be of 1 level

Number of nodes in k level = 2^(k-1)

Space / Time complexity = log n
"""
# Basic Class Representation of Binary Search Tree :


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


treenode = TreeNode(2)

# Creating a binary Search tree from tuple
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


# Displaying a Tree from tuple
def display_keys(node, space="\t", level=0):
    if node is None:
        print(space * level + "∅")
        return
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


display_keys(tree2, "  ")
