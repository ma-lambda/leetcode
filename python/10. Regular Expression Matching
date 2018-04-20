# I didn't solve this problem, maybe is a little difficult for me now. The following codes is imitated from 
# @jianchao.li.fighter https://leetcode.com/problems/regular-expression-matching/discuss/5684/9-lines-16ms-C++-DP-Solutions-with-Explanations
# the approch used the dynamic programming, it's efficient and concise
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            if len(s) != 0:
                return False
            else:
                return True
        m, n = len(s), len(p)
        l = [[False] * (n + 1) for _ in range(m + 1)]
        l[0][0] = True
        for i in range(0, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    l[i][j] = l[i][j - 2] or (i > 0 and l[i -1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    l[i][j] = i > 0 and l[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return l[m][n]
