# 这道题目本身不难，但是时间要求较高，试了各种方法，从一开始的O(n3)到后来的O(n2)都提示tle错误，不知道是否与网速有关。
# 下面这个方法是在discuss中的一个方法，时间为1129ms。from @Ipeq1 https://leetcode.com/problems/3sum/discuss/7516/N2-Python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res, l, i = [], len(nums), 0
        if l < 3:
            return []
        elif l == 3 and sum(nums) == 0:
            return [nums]
        while i < l - 2:
            if nums[i] > 0 or nums[i] + nums[i + 1] + nums[i + 2] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j, k = i + 1, l - 1
            while j < k:
                if nums[i] + nums[j] > 0:
                    return res
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == 0 and [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                elif tmp_sum > 0:
                    k -= 1
                    j -= 1                
                j += 1            
            i += 1
        return res
