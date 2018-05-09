# 413ms, a little slow
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        cursor1 = l // 2
        cursor2 = l // 2
        reverse_s = s[::-1] # reverse s only once
        if l <= 1 or s == reverse_s:
            return s
        # even, like 'abba'
        while s[:cursor1] != reverse_s[l-cursor1*2:l-cursor1]:
            cursor1 -= 1
            if cursor1 == 0:
                break
        s1 = reverse_s[:l-cursor1*2] + s
        # odd, like 'abcba'
        while s[:cursor2] != reverse_s[l-cursor2*2-1:l-cursor2-1]:
            cursor2 -= 1
            if cursor2 == 0:
                break
        s2 = reverse_s[:l-cursor2*2-1] + s
        if len(s1) < len(s2):
            return s1
        return s2
