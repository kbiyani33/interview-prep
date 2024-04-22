"""
There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 you have to first complete task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.


Example 1:

Input: 
N = 4, P = 3
prerequisites = {{1,0},{2,1},{3,2}}
Output:
Yes
Explanation:
To do task 1 you should have completed
task 0, and to do task 2 you should 
have finished task 1, and to do task 3 you 
should have finished task 2. So it is possible.
"""
from typing import List
from collections import deque

class Solution:
    def isCyclic(self, V:int, adj:List[List[int]]) -> bool :
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        topoSort = []
        while(len(q) > 0):
            node = q.popleft()
            topoSort.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return len(topoSort) < V

    def isPossible(self,N:int,P:int,prerequisites:List[List[int]]):
        #code here
        adj = [[] for i in range(N)]
        for i in prerequisites:
            first, second = i[1], i[0]
            adj[first].append(second)
        
        return not(self.isCyclic(V=N, adj=adj))

    
