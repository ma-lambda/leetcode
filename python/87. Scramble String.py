class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        if sorted(s1) != sorted(s2): return False
        for i in range(1, len(s1)):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22): return True
            s21 = s2[:len(s2) - i]
            s22 = s2[len(s2) - i:]
            if self.isScramble(s11, s22) and self.isScramble(s12, s21): return True
        return False
