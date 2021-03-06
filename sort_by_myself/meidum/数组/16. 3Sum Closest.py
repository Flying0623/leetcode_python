"""

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""

"""跟15题的思路类似"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                m = nums[i] + nums[l] + nums[r]
                if m == target:
                    return m
                if abs(m - target) < abs(res - target):
                    res = m
                if m < target:
                    l = l + 1
                else:
                    r = r - 1
        return res


