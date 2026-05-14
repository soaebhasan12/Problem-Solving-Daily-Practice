# Single Element in a Sorted Array

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
 

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

class Solution:
    def singleNonDuplicate(self, nums) -> int:
        ## Approach 1 : Binary Search
        n = len(nums)

        low = 0
        high = n - 1

        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 1:
                mid = mid - 1
            
            if nums[mid] == nums[mid+1]:
                low = mid + 2
            else:
                high = mid
        
        return nums[low]


        ## Approach 2 : Brute Force
        # n = len(nums)

        # if n == 1:
        #     return nums[0]
        
        # for i in range(n):
        #     if i == 0:
        #         if nums[i] != nums[i+1]:
        #             return nums[i]
            
        #     elif i == n - 1:
        #         if nums[i] != nums[i-1]:
        #             return nums[i]

        #     else:
        #         if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
        #             return nums[i]
