class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.visited = set()
        self.grid = grid
        return sum([self.dfs(i,j) for i in range(self.max_x) for j in range(self.max_y)])
    
    def dfs(self,i,j):
        if not self.check(i,j):
            return 0
        else:
            self.visited.add((i,j))
            self.dfs(i+1,j)
            self.dfs(i-1,j)
            self.dfs(i,j+1)
            self.dfs(i,j-1)
            return 1
    
    
    def check(self, x,y):
        if x <0 or x>=self.max_x or y<0 or y>=self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x,y) in self.visited):
            return False
        return True
