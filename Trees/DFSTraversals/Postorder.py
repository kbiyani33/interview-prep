from typing import List


# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


def iterative_postorder_2stacks(root: Node) -> List[any]:
    result = []
    st1, st2 = [], []
    if not root:
        return result
    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node.data)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)

    return st2[::-1]


def postOrder_helper(root: Node, result: List[any]):
    if not root:
        return
    postOrder_helper(root.left, result)
    postOrder_helper(root.right, result)
    result.append(root.data)


# Function to return a list containing the postOrder traversal of the tree.
def postOrder(root: Node) -> List[any]:

    result = []
    postOrder_helper(root, result)
    return result
