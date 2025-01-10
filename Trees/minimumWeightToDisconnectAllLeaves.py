class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of tuples (child_node, edge_weight)

def min_weight_to_disconnect_leaves(root):
    if not root:
        return 0

    def postorder(node):
        if not node.children:
            # If it's a leaf node, no cost to disconnect further
            return float("inf")

        total_weight = 0
        subtree_weight = 0

        for child, weight in node.children:
            # Calculate the weight to disconnect the child subtrees
            weight_to_disconnect = postorder(child)
            # Total weight to disconnect this child
            subtree_weight += weight_to_disconnect
            # Consider the direct disconnection of this edge
            total_weight += weight

        # Return the minimum between disconnecting the entire subtree or each leaf
        return min(total_weight, subtree_weight)

    return postorder(root)

# Example usage:
# Constructing the tree for the first example:
# A
# ├── B
# │   ├── D
# │   └── E
# └── C
a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')

a.children = [(b, 2), (c, 4)]
b.children = [(d, 2), (e, 1)]

# For example 1, this should output 6
result = min_weight_to_disconnect_leaves(a)
print(result)  # Output should be 6