class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        i, j, l = 0, 0, l1 + l2
        nums3 = []
        while i != l1 or j != l2:
            if j == l2 or i != l1 and nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if l % 2 == 1:
            return nums3[l//2]
        else:
            return (nums3[l//2 - 1] + nums3[l//2]) / 2.0
