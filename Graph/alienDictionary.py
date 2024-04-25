from typing import List
from collections import deque

class Solution:
    def topological_sort(self, adj:List[List[int]], V:int) -> List[int]:
        indegree = [0]*V
        toposort = []
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        # print(indegree)
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while(len(q) > 0):
            vertex = q.popleft()
            toposort.append(vertex)
            for neighbor in adj[vertex]:
                indegree[neighbor] -= 1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        
        return toposort

    def obtain_adj_list(self, n:int, k:int, alien_dict:List[str], char_dict:dict) -> List[List[str]]:
        adj = [[] for i in range(k)]
        for i in range(n-1):
            first = alien_dict[i]
            second = alien_dict[i+1]
            first_difference = [i for i, (left, right) in enumerate(zip(first, second)) if left != right]
            if len(first_difference)==0:
                continue
            first_letter = first[first_difference[0]]
            second_letter = second[first_difference[0]]
            adj[char_dict[first_letter]].append(char_dict[second_letter])
        return adj


            
    def findOrder(self,alien_dict:List[str], N:int, K:int):
        # code here
        char_dict = {}
        for i in range(K):
            char_dict[chr(i+97)] = i
        # print(char_dict)
        adj_list = self.obtain_adj_list(n=N, k=K, alien_dict=alien_dict, char_dict=char_dict)
        # print(adj_list)
        toposort = self.topological_sort(adj=adj_list, V=K)
        result = []
        for i in toposort:
            result.append(chr(i+97))
        # print(result)
        return result