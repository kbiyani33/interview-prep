"""
Given a Binary Tree, find the In-Order Traversal of it.

Example 1:

Input:
       1
     /  \
    3    2
Output: 3 1 2

Example 2:

Input:
        10
     /      \ 
    20       30 
  /    \    /
 40    60  50
Output: 40 20 60 10 50 30
"""

from typing import List


# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to return a list containing the inorder traversal of the tree.
class Solution:

    def iterative_inorder(self, root: Node):
        stack, result = [], []
        if not root:
            return result
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result

    def inorder_helper(self, root: Node, result: List[any]):
        if not root:
            return
        self.inorder_helper(root.left, result)
        result.append(root.data)
        self.inorder_helper(root.right, result)

    def InOrder(self, root):
        # code here
        result = []
        self.inorder_helper(root, result)
        return result
