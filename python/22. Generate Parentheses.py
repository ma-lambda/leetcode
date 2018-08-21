# a little slow
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = set()
        if n <= 1:
            return ['()' * n]
        result.add('(' * n + ')' * n)
        result.add('()' * n)
        if n > 2:
            for i in self.generateParenthesis(n - 1):
                result.add('(' + i + ')')
        for i in range(1, n):
            for l in self.generateParenthesis(i):
                for r in self.generateParenthesis(n - i):
                    result.add(l + r)
        return list(result)
