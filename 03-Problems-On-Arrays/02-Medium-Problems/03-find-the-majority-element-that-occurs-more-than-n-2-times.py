# Majority Element-I

"""
Given an integer array nums of size n, return the majority element of the array.


The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.


Example 1
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
Output: 7
Explanation:
The number 7 appears 5 times in the 9 sized array

Example 2
Input: nums = [1, 1, 1, 2, 1, 2]
Output: 1
Explanation:
The number 1 appears 4 times in the 6 sized array
"""


# SOLVED USING 2 APPROACHES: 1. HASHING and 2. MOORE's ALGORITHM

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # APPROACH 01: HASHMAP

        # map_dict = {}

        # for i in range(len(nums)):
        #     if nums[i] not in map_dict:
        #         map_dict[nums[i]] = 1
        #     else:
        #         map_dict[nums[i]] += 1

        # for key in map_dict:
        #     if map_dict[key] > len(nums) // 2:
        #         return key
        #     else:
        #         continue


        # APPROACH 02: Boyer-Moore's Voting Algorithm
        candidate = None
        count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1
        
        return candidate