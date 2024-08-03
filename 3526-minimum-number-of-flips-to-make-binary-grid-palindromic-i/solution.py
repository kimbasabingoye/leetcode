class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row_ans = 0
        col_ans = 0

        for e in grid:
            left = 0
            right = len(e)-1
            while left < right:
                if e[left] != e[right]:
                    row_ans += 1
                left += 1
                right -= 1

        arr = [] 
        for j in range(len(grid[0])):
            tmp = []
            for i in range(len(grid)):
                tmp.append(grid[i][j])
            arr.append(tmp)
        
        for e in arr:
            left = 0
            right = len(e)-1
            while left < right:
                if e[left] != e[right]:
                    col_ans += 1
                left += 1
                right -= 1
        
        return min(row_ans, col_ans)

        
