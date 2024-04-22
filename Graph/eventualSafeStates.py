
from typing import List

class Solution:    
    def dfs_directed(self, V:int, adj:List[List[int]], visited:List[bool], pathVisited: List[bool], safeState:List[bool], startingNode: int):
        # mark the startingNode as visited and path visited
        visited[startingNode] = True
        pathVisited[startingNode] = True
        safeState[startingNode] = False 
        # why do we have to reinitialise it ? 
        # Because we want all possible paths through this startiNode, it may have been marked safe through a different path, but not this path.

        for neighbor in adj[startingNode]:
            if not visited[neighbor]:
                if self.dfs_directed(V, adj, visited, pathVisited, neighbor):
                    return True # this basically is equivalent to returning True after setting startingNode as not safe initially.
            elif pathVisited[neighbor]:
                return True
        pathVisited[startingNode] = False
        safeState[startingNode] = True # since we have gone over all paths through this startingNode, so we make it true
        return False
    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        visited = [False] * V
        pathVisited = [False] * V
        safeState = [False] * V

        for i in range(V):
            if not visited[i]:
                self.dfs_directed(V, adj, visited, pathVisited, safeState, i)
        
        return [i for i in range(len(safeState)) if safeState[i] is True]

        
