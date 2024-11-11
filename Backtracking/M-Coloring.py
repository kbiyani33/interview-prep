from typing import List
class Solution:
    def isPossibleToColor(self, node:int, col:int, adjList:List[List[int]], color:List[int]) -> bool:
        for adj in adjList[node]:
            if color[adj]==col:
                return False
        return True
        
    def dfs(self, node:int, m:int, adjList:List[List[int]], color:List[int]) -> bool:
        if node == len(adjList):
            return True
        # go from 1 to m. If it's possible to color a node 
        for c in range(1, m+1):
            if self.isPossibleToColor(node=node, c=c):
                color[node] = c
                if self.dfs(node+1, m, adjList, color): return True
                color[node] = -1
        return False
    def graphColoring(self, v:int, edges:List[List[int]], m:int) -> bool:
        if m >= v:
            return True 
        adjList = [[] for _ in range(v)]
        for s,d in edges:
            adjList[s].append(d)
            adjList[d].append(s)
        color = [-1]*v
        # make node zero get colored with i and see if it's possible to do DFS withou repeating previous color
        return self.dfs(0, m, adjList, color)