class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = float("-inf")
        visited = set()
        m , n =len(grid) ,len(grid[0])

        def dfs(i,j)->int:
            if i<0 or i > m-1 or j <0 or j> n-1 or grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            r1 = dfs(i,j+1)
            r2 = dfs(i,j-1)
            r3 = dfs(i-1,j)
            r4 = dfs(i+1,j)
            return r1+r2+r3+r4 + 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(dfs(i,j), res) 
        return res if res != float("-inf") else 0

