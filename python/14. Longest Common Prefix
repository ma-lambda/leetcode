class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        minS = strs[0]
        minL = len(strs[0])
        num = 0
        for s in strs:
            if len(s) < minL:
                minL = len(s)
                minS = s
        for i in range(minL):
            for s in strs:
                if s[num] != minS[num]:
                    return minS[:num]
            num += 1
        return minS[:num]
