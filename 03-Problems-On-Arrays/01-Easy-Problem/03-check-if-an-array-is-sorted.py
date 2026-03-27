# Check if the Array is Sorted II

"""
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


Example 1
Input : nums = [1, 2, 3, 4, 5]
Output : true
Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Example 2
Input : nums = [1, 2, 1, 4, 5]
Output : false
Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.
"""


class Solution:
    def isSorted(self, nums):
        if len(nums) <= 1:
            return True

        n = len(nums) - 1

        # for i in range(n):
        #     if nums[i] <= nums[i+1]:
        #         continue
        #     else:
        #         return False
        # return True

        for i in range(n):
            if nums[i] > nums[i+1]:
                return False
        return True
        