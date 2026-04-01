# Maximum Consecutive Ones

"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.

A binary array is an array that contains only 0s and 1s.

Example 1
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
Output: 3
Explanation:
The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Example 2
Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]
Output: 0
Explanation:
No 1s are present in nums, thus we return 0
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxi = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > maxi:
                    maxi = count
                else:
                    continue
            else:
                count = 0

        return maxi