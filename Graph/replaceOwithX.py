from typing import List
from collections import deque

class Solution:
    def fill_using_dfs(self, m:int, n:int, cr:int, cc:int, grid:List[List[str]], visited:List[List[bool]], result:List[List[str]]):
        if visited[cr][cc]:
            return
        # we are going to call this from the boundary elements
        # mark it as visited
        visited[cr][cc] = True
        # make it's result as 'O'
        result[cr][cc] = 'O'
        # move in 4 directions and call this recusrively for any non visited cell with 'O' as the value
        neighbors  = [[cr-1, cc], [cr+1, cc], [cr, cc-1], [cr, cc+1]]
        for ng in neighbors:
            nr, nc = ng[0], ng[1]
            if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]=='O' and not visited[nr][nc]:
                self.fill_using_dfs(m=m, n=n, cr=nr, cc=nc, grid=grid, visited=visited, result=result)

    def fill_using_bfs(self, m:int, n:int, grid:List[List[str]], visited:List[List[bool]], result:List[List[str]]):
        
        q = deque()

        # for rows 0 and m-1 search for any 0's
        for j in range(n):
            if grid[0][j] == 'O':
                # mark this as visited
                visited[0][j] = True
                # append it to the q
                q.append((0, j))
                # make this as O only in the result
                result[0][j] = 'O'
            
            if grid[m-1][j] == 'O':
                # mark this as visited
                visited[m-1][j] = True
                # append it to the q
                q.append((m-1, j))
                # make this as O only in the result
                result[m-1][j] = 'O'
        
        # for columns 0 and n-1 search if there are any 0's
        for i in range(m):
            if grid[i][0] == 'O':
                # mark it as visited
                visited[i][0] = True
                # append it to the queue
                q.append((i, 0))
                # make this as O only in the result
                result[i][0] = 'O'

            if grid[i][n-1] == 'O':
                # mark it as visited
                visited[i][n-1] = True
                # append it to the queue
                q.append((i, n-1))
                # make this as O only in the result
                result[i][n-1] = 'O'
        
        # Now perform BFS on the queue
        while(len(q) > 0):
            r, c = q.popleft()
            neighbors = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
            for ng in neighbors:
                nr, nc = ng[0], ng[1]
                if nr>=0 and nr<m and nc>=0 and nc<n and not visited[nr][nc] and grid[nr][nc] == 'O':
                    visited[nr][nc] = True
                    result[nr][nc] = 'O'
                    q.append((nr, nc))
        
        # travel all non visited elements and make them as X in the result
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    result[i][j] = 'X'
                    visited[i][j] = True

    def fill(self, m:int, n:int, mat:List[List[str]]) -> List[List[str]]:
        # code here
        grid_copy = [['']*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                grid_copy[i][j] = mat[i][j]
        
        visited = [[False]*n for i in range(m)]
        result = [['']*n for i in range(m)]
        self.fill_using_bfs(m=m, n=n, grid=grid_copy, visited=visited, result=result)
        return result
    
    def fill_dfs(self, m:int, n:int, mat:List[List[str]]) -> List[List[str]]:
        # code here
        grid_copy = [['']*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                grid_copy[i][j] = mat[i][j]
        
        visited = [[False]*n for i in range(m)]
        result = [['']*n for i in range(m)]
        for j in range(n):
            if grid_copy[0][j] == 'O' and not visited[0][j]:
                self.fill_using_dfs(m=m, n=n, cr=0, cc=j, grid=grid_copy, visited=visited, result=result)
            if grid_copy[m-1][j] == 'O' and not visited[m-1][j]:
                self.fill_using_dfs(m=m, n=n, cr=m-1, cc=j, grid=grid_copy, visited=visited, result=result) 
        
        for i in range(m):
            if grid_copy[i][0] == 'O' and not visited[i][0]:
                self.fill_using_dfs(m=m, n=n, cr=i, cc=0, grid=grid_copy, visited=visited, result=result)
            if grid_copy[i][n-1] == 'O' and not visited[i][n-1]:
                self.fill_using_dfs(m=m, n=n, cr=i, cc=n-1, grid=grid_copy, visited=visited, result=result)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    result[i][j] = 'X'
                    visited[i][j] = True
        
        return result
