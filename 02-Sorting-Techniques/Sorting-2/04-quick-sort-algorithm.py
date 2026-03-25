# Quick Sorting

"""
Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm and return the sorted array.


A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

Example 1
Input: nums = [7, 4, 1, 5, 3]
Output: [1, 3, 4, 5, 7]
Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.

Example 2
Input: nums = [5, 4, 4, 1, 1]
Output: [1, 1, 4, 4, 5]
Explanation: 1 <= 1 <= 4 <= 4 <= 5.
Thus the array is sorted in non-decreasing order.
"""


class Solution:
    def quickSort(self, nums, start=None, end=None):

        # default values handle
        if start is None:
            start = 0
        if end is None:
            end = len(nums) - 1

        # base condition
        if start >= end:
            return

        # partition
        pivot = nums[end]
        i = start - 1

        for j in range(start, end):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # place pivot correctly
        nums[i + 1], nums[end] = nums[end], nums[i + 1]

        # recursive calls
        self.quickSort(nums, start, i)
        self.quickSort(nums, i + 2, end)

        return nums



obj = Solution() 
   
arr = [5,4,9,2,8,3,7,1,6]
print("\nBefore Using Quick Sort:")
print(" ".join(map(str, arr)))

output = obj.quickSort(arr)
print("\nBefore Using Quick Sort:")
print(" ".join(map(str, output)))