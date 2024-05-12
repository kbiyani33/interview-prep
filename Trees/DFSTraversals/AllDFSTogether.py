from typing import List


# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


def allTraversalsToGether(root: Node) -> dict:
    preOrder, inOrder, postOrder = [], [], []

    if not root:
        return {"pre": preOrder, "in": inOrder, "post": postOrder}

    stack = []
    stack.append((root, 1))

    while stack:
        node, level = stack.pop()
        if level == 1:
            stack.append((node, level + 1))
            preOrder.append(node.data)
            if node.left:
                stack.append((node.left, 1))
        elif level == 2:
            inOrder.append(node.data)
            stack.append((node, level + 1))
            if node.right:
                stack.append((node.right, 1))
        elif level == 3:
            postOrder.append(node.data)

    return {"pre": preOrder, "in": inOrder, "post": postOrder}
