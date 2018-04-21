class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        left = ['(', '{', '[']
        right = [')', '}', ']']
        predict = ''
        for ch in s:
            if ch in left:
                predict = right[left.index(ch)] + predict
            else:
                if len(predict) == 0 or ch != predict[0]:
                    return False
                else:
                    predict = predict[1:]
        if not predict:
            return True
        else:
            return False
