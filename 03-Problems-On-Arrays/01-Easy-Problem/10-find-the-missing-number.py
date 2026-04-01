# Find missing number

"""
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

Example 1
Input: nums = [0, 2, 3, 1, 4]
Output: 5
Explanation:
nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Example 2
Input: nums = [0, 1, 2, 4, 5, 6]
Output: 3
Explanation:
nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]
"""

class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        # for i in range(n+1):
        #     if i not in nums:
        #         return i

        sum_n = n * (n + 1) / 2

        sum_nums = 0

        for i in range(n):
            sum_nums += nums[i]
        
        elem = sum_n - sum_nums

        return int(elem)

