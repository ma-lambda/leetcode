class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        pivot = len(nums) // 2
        if nums[pivot] == target:
            return pivot
        if len(nums) == 1:
            return -1
        for i in range(len(nums)):
            left_index = self.search(nums[:pivot], target)
            right_index = self.search(nums[pivot + 1:], target)
            if left_index != -1:
                return left_index
            elif right_index != -1:
                return pivot + 1 + right_index
            else:
                return -1
