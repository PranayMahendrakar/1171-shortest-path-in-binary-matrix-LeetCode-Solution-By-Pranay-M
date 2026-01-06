class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        n = len(grid)
        
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # 8 directions
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        # BFS
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited
        
        while queue:
            r, c, length = queue.popleft()
            
            if r == n-1 and c == n-1:
                return length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark as visited
                    queue.append((nr, nc, length + 1))
        
        return -1