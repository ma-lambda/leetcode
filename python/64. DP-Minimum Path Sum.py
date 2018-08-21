# dynamic programming
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        m, n = len(grid), len(grid[0])
        dp = np.zeros([m, n])
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif dp[i][j - 1] < dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
        return int(dp[-1][-1])
