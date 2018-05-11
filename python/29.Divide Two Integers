# my solution is too slowly, occur TLE
# the following answer is copied from https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code by @tusizi
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                res += i
                dividend -= temp
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31-1)
