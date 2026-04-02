# Longest subarray with sum K

"""
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

Example 1
Input: nums = [10, 5, 2, 7, 1, 9],  k=15
Output: 4
Explanation:
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

Example 2
Input: nums = [-3, 2, 1], k=6
Output: 0
Explanation:
There is no sub-array in the array that sums to 6. Therefore, the output is 0.
"""


class Solution:
    def longestSubarray(self, nums, k):
        sum = 0
        answer = 0
        count = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    length = j - i + 1
                    answer = max(answer, length)
                    sum = 0
                    break
                    # count += 1
                    # sum = 0
                    # break                    
                elif sum > k:
                    break
        
        return count
      
      
      
# OPTIMAL SOLUTION

class Solution:
    def longestSubarray(self, nums, k):
        prefix_map = {}
        curr_sum = 0
        max_len = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            # Case 1: from index 0
            if curr_sum == k:
                max_len = i + 1

            # Case 2: subarray exists
            if (curr_sum - k) in prefix_map:
                length = i - prefix_map[curr_sum - k]
                max_len = max(max_len, length)

            # Store first occurrence only
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return max_len