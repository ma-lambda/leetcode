class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPosit = 1
        if - 10 < x < 10:
            return x        
        if x < 0:
            isPosit = -1
            x = -x
        x = str(x)
        r = x[::-1]
        if r[0] == '0':
            r = r[1:]
        r = int(r) * isPosit
        if - 2 ** 31 > r or r > (2 ** 31 -1):
            return 0
        else:
            return r
