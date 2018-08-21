class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        ln = len(needle)
        lh = len (haystack)
        if lh < ln:
            return -1
        if haystack == needle:
            return 0
        for i in range(0, lh - ln + 1):
            if haystack[i:i+ln] == needle:
                return i
        return -1
