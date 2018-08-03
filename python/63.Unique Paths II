class Solution(object):    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = np.zeros([m, n])
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] != 1:
                    if j > 0 and obstacleGrid[i][j - 1] != 1:
                        dp[i][j] += dp[i][j - 1]
                    if i > 0 and obstacleGrid[i - 1][j] != 1:
                        dp[i][j] += dp[i - 1][j]
        return int(dp[-1][-1])
