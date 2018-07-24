class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, target, [], res)
        return res
        
    def helper(self,candi, target,cur,res):
        if target<0:
            return
        if target ==0:
            res.append(cur)
            return
        for i in range(len(candi)):
            self.helper(candi[i:],target-candi[i],cur+[candi[i]],res)
