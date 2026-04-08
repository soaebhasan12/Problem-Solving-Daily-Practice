# Kadane's Algorithm - Maximum Subarray Sum

"""
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1
Input: nums = [2, 3, 5, -2, 7, -4]
Output: 15
Explanation:
The subarray from index 0 to index 4 has the largest sum = 15

Example 2
Input: nums = [-2, -3, -7, -2, -10, -4]
Output: -2
Explanation:
The element on index 0 or index 3 make up the largest sum when taken as a subarray
"""



# HOW TO PRINT SUBARRAYS 
"""    
nums = [2, 3, 5, -2, 7]

start = 0
end = 0

n = len(nums)
 
for start in range(start, n):
  for end in range(start, n):
    sub = []
    for k in range(start, end+1):
      sub.append(nums[k])
    
    print(sub)
"""
    
    
# BRUTE FORCE APPROACH - O(n^2) - TLE
class Solution:
    def maxSubArray(self, nums):
        start = 0
        end = 0
        
        max_sum = 0
        
        for start in range(len(nums)):
          curr_sum = 0
          for end in range(start, len(nums)):
            curr_sum += nums[end]
            if max_sum > curr_sum:
              max_sum = curr_sum
              
        return max_sum



        # KADANE'S ALGORITHM - O(n)

        # maxSum = nums[0]
        # currSum = 0

        # for i in range(len(nums)):
        #     currSum += nums[i]
        #     maxSum = max(currSum, maxSum)
        #     if currSum < 0:
        #         currSum = 0
        # return maxSum