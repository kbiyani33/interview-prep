from typing import List
class DisjointSet:

    def __init__(self, N:int):
        self.N = N
        self.parent = [i for i in range(N+1)]
        self.size = [1]*(N+1)
    
    def findParent(self, node:int) -> int:
        parent = self.parent
        if parent[node]==node:
            return node
        parent[node] = self.findParent(parent[node])
        return parent[node]
    
    def unionBySize(self, u:int, v:int):
        parent, size = self.parent, self.size
        parentU = self.findParent(u)
        parentV = self.findParent(v)

        if parentU == parentV:
            return
        
        if size[parentU] < size[parentV]:
            parent[parentU] = parentV
            size[v] += size[u]
        else:
            parent[parentV] = parentU
            size[u] += size[v]
        # if parentU == parentV:
        #     return
        
        # if rank[parentU] < rank[parentV]:
        #     parent[u] = v
        # elif rank[parentV] < rank[parentU]:
        #     parent[v] = u
        # else:
        #     parent[parentV] = parentU
        #     rank[u]+=1
    
if __name__=="__main__":
    ds = DisjointSet(7)
    ds.unionBySize(1,2)
    ds.unionBySize(2,3)
    ds.unionBySize(4,5)
    ds.unionBySize(6,7)
    ds.unionBySize(5,6)
    print(ds.findParent(3)==ds.findParent(7))
    ds.unionBySize(3,7)
    print(ds.findParent(3)==ds.findParent(7))
