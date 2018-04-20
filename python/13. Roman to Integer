class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        romans = ['CM', 'M', 'CD', 'D', 'XC', 'C', 'XL', 'L', 'IX', 'X', 'IV', 'V', 'I']
        nums = [900, 1000, 400, 500, 90, 100, 40, 50, 9, 10, 4, 5, 1]
        for i in range(len(romans)):
            if romans[i] in s:
                num += nums[i] * s.count(romans[i])
                s = s.replace(romans[i], '')
        return num
