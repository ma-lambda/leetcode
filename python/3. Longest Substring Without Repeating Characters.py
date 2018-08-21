class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ''
        maxl = 0
        l = 0
        for ch in s:
            if ch not in sub:
                sub += ch
                l += 1
            else:
                sub += ch
                if l > maxl:
                    maxl = l
                sub = sub[sub.index(ch) + 1:]
                l = len(sub)
        return maxl if maxl > l else l
