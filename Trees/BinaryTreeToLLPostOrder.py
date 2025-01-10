# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        curr = root
        while curr:
            if not curr.left:
                curr = curr.right
            else:
                pred = curr.left
                while pred and pred.right:
                    pred = pred.right
                # print(pred)
                pred.right = curr.right
                curr.right = curr.left
                curr.left = None
                curr = curr.right
        
        