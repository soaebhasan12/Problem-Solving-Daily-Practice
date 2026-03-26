# Largest Element

"""
Given an array of integers nums, return the value of the largest element in the array

Example 1
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6

Example 2
Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99
"""


# A) Brute Force
class Solution:
    def largestElement(self, nums):
        if len(nums) <= 1:
            return nums
            
        largest = nums[0]

        for i in range(len(nums)):
            if largest < nums[i]:
                largest = nums[i]
        return largest

# B) Optimal Approach