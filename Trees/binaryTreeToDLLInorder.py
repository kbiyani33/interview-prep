from os import *
from sys import *
from collections import *
from math import *

''' 
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def recursive(node, nodes):
    if not node:
        return
    # first go for left
    recursive(node.left, nodes)
    if nodes[1]:
        nodes[1].right = node
        node.left = nodes[1]
    else:
        nodes[0] = node
    nodes[1] = node
    recursive(node.right, nodes)
    

def BTtoDLL(root):
    # Write your code here.
    if not root:
        return None
    nodes = [None, None]
    recursive(root, nodes)
    return nodes[0]