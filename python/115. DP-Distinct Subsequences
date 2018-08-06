# this is my solution which is too slow, cause TOE, though it is right
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t or not s:
            return 0
        dp = [0 for i in range(len(t))]
        return self.helper(s, t, dp, 0)[-1]        
    def helper(self, s, t, dp, num):
        if not t or not s:
            return dp
        while s.count(t[0]):
            i = s.index(t[0])
            dp[num] += 1
            s = s[i + 1:]
            dp = self.helper(s, t[1:], dp, num + 1)
        return dp

# this is another solution from @Rogerwlk which is very concise and fast, it's inspiring.
from collections import defaultdict
class Solution:
    def numDistinct(self, s, t):
        if not s or not t: return 0        
        li = [0 for x in range(len(t))]
        d = defaultdict(list)        
        for (i, ch) in enumerate(t):
            d[ch].append(i)        
        for i in range(len(s)):
            if s[i] in t:
                for j in reversed(d[s[i]]):
                    if j == 0:
                        li[0] += 1
                    else:
                        li[j] += li[j - 1]
        return li[-1]
