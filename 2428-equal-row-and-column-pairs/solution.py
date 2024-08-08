class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        n  = len(grid)
        ans = 0
        
        for i in range(n):
            rows[tuple(grid[i])] += 1
        
        grid_cols = list(zip(*grid)) 
        for i in range(n):
            cols[tuple(grid_cols[i])] += 1

        #print(rows)
        #print(cols)

        for k, v in rows.items():
            ans += v * cols[k]

        
        return ans
