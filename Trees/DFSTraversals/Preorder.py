# Node Class:
from typing import List


# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


def preorder_helper(root: Node, result: List[any]):
    if not root:
        return
    result.append(root.data)
    preorder_helper(root.left, result)
    preorder_helper(root.right, result)


def iterative_preorder(root: Node):
    stack = []
    result = []

    if not root:
        return result

    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


# Function to return a list containing the preorder traversal of the tree.
def preorder(root: Node) -> List[any]:

    # result = []
    # preorder_helper(root, result)
    # return result
    return iterative_preorder(root)
