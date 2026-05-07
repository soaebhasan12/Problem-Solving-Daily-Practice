# Find First and Last Position of Element in Sorted Array

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    ## BINARY SEARCH APPROACH
    def firstOccurrence(self, nums, target):

        low = 0
        high = len(nums) - 1

        first = -1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:

                first = mid
                high = mid - 1

            elif nums[mid] < target:

                low = mid + 1

            else:

                high = mid - 1

        return first


    def lastOccurrence(self, nums, target):

        low = 0
        high = len(nums) - 1

        last = -1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:

                last = mid
                low = mid + 1

            elif nums[mid] < target:

                low = mid + 1

            else:

                high = mid - 1

        return last


    def searchRange(self, nums, target):

        first = self.firstOccurrence(nums, target)

        if first == -1:
            return [-1, -1]

        last = self.lastOccurrence(nums, target)

        return [first, last]




    ## LOWER AND UPPER BOUND APPROACH 
    # def lowerBound(self, nums, n, target):
    #     low = 0
    #     high = n - 1
    #     ans = n

    #     while low <= high:
    #         mid = (low + high) // 2

    #         if nums[mid] >= target:
    #             ans = mid
    #             high = mid - 1
    #         else:
    #             low = mid + 1
        
    #     return ans

    # def upperBound(self, nums, n, target):
    #     ans = n

    #     low = 0
    #     high = n - 1

    #     while low <= high:
    #         mid = (low + high) // 2

    #         if nums[mid] > target:
    #             ans = mid
    #             high = mid - 1
    #         else:
    #             low = mid + 1
        
    #     return ans

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)

    #     lb = self.lowerBound(nums, n, target)
    #     ub = self.upperBound(nums, n, target) - 1

    #     if lb == n or nums[lb] != target:
    #         return [-1, -1]
        
    #     return [lb, ub]


    ## BRUTE FORCE APPROACH - LINEAR TRAVERSE
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # first = -1
        # last = -1
        # n = len(nums)

        # for i in range(n):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i

        # if first != -1 and last != -1:
        #     return [first, last]    
        
        # return [-1, -1]
