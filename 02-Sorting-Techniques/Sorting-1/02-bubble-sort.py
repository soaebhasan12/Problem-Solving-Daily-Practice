# Bubble Sort

"""
Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

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
    def bubbleSort(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums
      
      
      
obj = Solution()

arr = [5,4,9,2,8,3,7,1,6]
print("Before Using Bubble Sort:")
print(" ".join(map(str, arr)))

output = obj.bubbleSort(arr)
print("Before Using Bubble Sort:")
print(" ".join(map(str, output)))