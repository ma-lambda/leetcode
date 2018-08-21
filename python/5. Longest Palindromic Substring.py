# 字符串有两种对称方式，包括长度为奇数与长度为偶数两种，因此遍历字符串，针对每个字符检测是否存在这两种对称方式
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]: # 若字符串长度为1或其与其逆序相同，则直接返回
            return s
        maxPalS = s[0]
        maxL = 1
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                subs = findOdd(s, i)
                if len(subs) > maxL:
                    maxPalS = subs
                    maxL = len(subs)
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                subs = findEven(s, i)
                if len(subs) > maxL:
                    maxPalS = subs
                    maxL = len(subs)
        return maxPalS
                
def findOdd(s, i):
    '''奇对称'''
    offset = 1
    while (i - offset - 1) >= 0 and (i + offset + 1) < len(s) and s[i - offset - 1] == s[i + offset + 1]:
        offset += 1
    return s[i - offset:i + offset + 1]

def findEven(s, i):
    '''偶对称'''
    offset = 1
    while (i - offset - 1) >= 0 and (i + offset) < len(s) and s[i - offset - 1] == s[i + offset]:
        offset += 1
    return s[i - offset:i + offset]
