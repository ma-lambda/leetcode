class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            return []
        strs = []
        for num in digits:
            strs.append(dic[num])
        l = 1
        index = 0
        for s in strs:
            l *= len(s)
        res = [''] * l
        n = 1
        for i in range(len(strs)):
            n *= len(strs[i])
            while index < l:
                if l != n:
                    res[index] += strs[i][int(index / (l / n)) % len(strs[i])]
                    index += 1
                else:
                    for j in range(len(strs[i])):
                        res[index] += strs[i][j]
                        index += 1                
            index = 0
        return res
