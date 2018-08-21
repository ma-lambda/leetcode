# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n, {})
    def helper(self, start, end, memo):
        if start > end:
            return [None]
        if (start, end) in memo:
            return memo[(start, end)]
        memo[(start, end)] = []
        for root_value in range(start, end + 1):
            for left_child in self.helper(start, root_value - 1, memo):
                for right_child in self.helper(root_value + 1, end, memo):
                    root = TreeNode(root_value)
                    root.left, root.right = left_child, right_child
                    memo[(start, end)].append(root)
        return memo[(start, end)]
        
            
            
