"""
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one
"""

from typing import Optional


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        if lh == -1 or rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1
