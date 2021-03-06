class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """        
        def helper(s1, s2, s3):
            l1, l2, l3 = len(s1), len(s2), len(s3)
            if dp[l1][l2] == 1: return True
            if not dp[l1][l2]: return False
            if not s1 and s2 != s3: return False
            if not s2 and s1 != s3: return False
            if l1 + l2 != l3: return False
            if not s3: return True
            if s1 + s2 == s3 or s2 + s1 == s3:
                dp[l1][l2] = 1
                return True
            if s1[-1] != s3[-1] and s2[-1] != s3[-1]: 
                dp[l1][l2] = 0
                return False
            if s1[-1] == s3[-1] and helper(s1[:-1], s2, s3[:-1]):
                dp[l1][l2] = 1
                return True
            if s2[-1] == s3[-1] and helper(s1, s2[:-1], s3[:-1]):
                dp[l1][l2] = 1
                return True
            dp[l1][l2] = 0
            return False
        dp = [[-1 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        return helper(s1, s2, s3)
