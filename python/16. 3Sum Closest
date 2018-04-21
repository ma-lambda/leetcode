class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        if l == 3:
            return sum(nums)
        closest = sum(nums[:3])
        diff = closest - target
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, l - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s > target:
                    k -= 1
                else:
                    j += 1
                if abs(s - target) < abs(diff):
                    closest = s
                    diff = s - target
        return closest
