class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def symmetric(node1, node2) -> bool:
    if not node1 and not node2:
        return True
    ans1 = symmetric(node1.left, node2.right)
    ans2 = symmetric(node1.right, node2.left)

    return ans1 and ans2 and node1.val==node2.val


def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    return symmetric(root.left, root.right)