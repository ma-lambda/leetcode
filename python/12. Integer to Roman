class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        s += num // 1000 * 'M'
        s += (num % 1000) // 500 * 'D'
        s += (num % 500) // 100 * 'C'
        s += (num % 100) // 50 * 'L'
        s += (num % 50) // 10 * 'X'
        s += (num % 10) // 5 * 'V'
        s += (num % 5) * 'I'
        return s.replace('DCCCC', 'CM').replace('CCCC', 'CD').replace('LXXXX', 'XC').replace('XXXX', 'XL').replace('VIIII', 'IX').replace('IIII', 'IV')
