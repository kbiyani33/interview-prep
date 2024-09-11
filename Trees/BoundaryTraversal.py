def printLeftBoundary(root, res):
    if not root:
        return
    if root.left or root.right: # not a leaf node
        res.append(root.data)
    if root.left:
        printLeftBoundary(root.left, res)
    else:
        printLeftBoundary(root.right, res)

def printLeaves(root, res):
    if not root:
        return
    if not root.left and not root.right:
        res.append(root.data)
    printLeaves(root.left, res)
    printLeaves(root.right, res)

def printRightBoundary(root, res):
    temp = []
    if not root:
        return
    if root.left or root.right: # not leaf
        temp.append(root.data)
    if root.right:
        printRightBoundary(root.right, res)
    else:
        printRightBoundary(root.left, res)
    for i in range(len(temp)-1, -1, -1):
        res.append(temp[i])


def printBoundary(root, res):
    if not root:
        return
    res.append(root.data)
    printLeftBoundary(root.left, res)
    printLeaves(root, res)
    printRightBoundary(root.right, res)

def traverseBoundary(root):
    if not root:
        return []
    res = []
    printBoundary(root, res)
    return res