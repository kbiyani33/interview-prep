from typing import List
from collections import deque
"""
always remember that in BFS, we will mark it as visited as true everytime we append it to the list. 
Don't mix the methods here.
"""
def bfsOfGraph(V: int, adj: List[List[int]], starting:int) -> List[int]:
    # code here
    q = deque()
    visited = [False] * V
    q.append(starting)
    visited[starting] = True
    result = []
    
    while(len(q) > 0):
        element = q.popleft()
        result.append(element)
        for i in adj[element]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return result

    
