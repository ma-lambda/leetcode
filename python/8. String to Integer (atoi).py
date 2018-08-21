class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if s == '':
            return 0
        nums = ['-', '+']
        beg = 0
        r = ''
        for i in range(10):
            nums.append(str(i))
        s = s.strip()
        if s[0] not in nums:
            return 0
        if s[0] in nums[:3]:
            r += s[0]
            beg = 1
            if len(s) == 1:
                return 0
        for ch in s[beg:]:
            if ch in nums[2:]:
                r += ch
            else:
                break
        if beg == 1 and len(r) == 1:
            return 0
        r = int(r)
        if r > 2 ** 31 - 1:
            return 2 ** 31 -1
        elif r < - 2 ** 31:
            return - 2 ** 31
        else:
            return r
