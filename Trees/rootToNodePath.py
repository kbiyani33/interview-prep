from os import *
from sys import *
from collections import *
from math import *

from typing import List


"""
What's the idea ?
Its a high level recursive code.

This is solved using inorder traversal. 

1. If I come to a leaf node the value of which is not equal to desired value, then return False
2. If i come to a none value then return False
3. Then append the current node to path
4. If it's able to find the element in left or right, then return the path.
5. Otherwise, you neeed to pop the node if neither left nor right has the path in question.
"""

class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathHelper(root, x, path):
    if not root:
        return False
    path.append(root.data)
    if root.data == x:
        return True
    
    leftSide = pathHelper(root.left, x, path)
    rightSide = pathHelper(root.right, x, path)
    if leftSide or rightSide:
        return True
    path.pop()

def pathInATree(root: TreeNode, x: int) -> List[int]:
    # Write your code here.
    path = []
    pathHelper(root, x, path)
    return path