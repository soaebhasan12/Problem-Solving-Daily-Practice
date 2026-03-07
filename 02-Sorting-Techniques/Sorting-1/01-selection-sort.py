# Selection Sort Problem

"""
Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.

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
  def selectionSort(self, nums):
    for i in range(0, len(nums)-1):
      min_index = i
      for j in range(i+1, len(nums)):
        if nums[j] < nums[min_index]:
           min_index = j
      temp = nums[min_index]
      nums[min_index] = nums[i]
      nums[i] = temp
    return nums
  
obj = Solution()
output = obj.selectionSort([5,4,9,2,8,3,7,1,6])
print(output)