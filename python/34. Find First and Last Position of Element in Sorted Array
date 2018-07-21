class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res  = []
        try:
            index = nums.index(target)
        except:
            return [-1, -1]
        res.append(nums.index(target))
        nums = nums[::-1]
        res.append(len(nums) - 1 - nums.index(target))
        return res
