def rootToNodePath(root, node, path):
    if not root:
        return False
    path.append(root.data)
    if root.data==node:
        return True
    lp, rp = rootToNodePath(root.left, node, path), rootToNodePath(root.right, node, path)
    if lp or rp:
        return True
    path.pop()

def lowestCommonAncestor(root, x: int, y: int) -> int:
    pathX, pathY = [], []
    rootToNodePath(root, x, pathX)
    rootToNodePath(root, y, pathY)
    i, j = 0, 0
    lca = -1
    while i<len(pathX) and j<len(pathY):
        if pathX[i] == pathY[j]:
            lca = pathX[i]
            i+=1
            j+=1
        else:
            break
    return lca