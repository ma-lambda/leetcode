class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums)
        while l <= r and l < len(nums):
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            if l == r:
                if target < nums[r]:
                    return r
                if target > nums[l]:
                    return l + 1
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return len(nums)

# another version which is more concise
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] >= target else start + 1
