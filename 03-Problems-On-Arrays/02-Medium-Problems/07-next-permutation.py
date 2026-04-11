# Next Permutation - Return Lexicographically Next Array

"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], 
the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].


The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].

Similarly, the next permutation of arr = [2,3,1] is [3,1,2].

While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.


Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""


# APPROACH 1: BRUTE FORCE - O(n! * n)
# A) : Generate all arrays, recursively
# B) : Lenear Search
# C) : Return Next Index Array.

from itertools import permutations

class Solution:
    def nextPermutation(self, nums):
        
        # Step 1: Generate all permutations
        perms = list(permutations(nums))
        
        # Step 2: Convert tuples to lists
        perms = [list(p) for p in perms]
        
        # Step 3: Sort lexicographically
        perms.sort()
        
        # Step 4: Find current index
        for i in range(len(perms)):
            if perms[i] == nums:
                # Step 5: Return next permutation
                if i + 1 < len(perms):
                    return perms[i + 1]
                else:
                    return perms[0]
                  

"""
# Please write the code of it for beginners standard
"""


# APPROACH 2: OPTIMAL SOLUTION
class Solution:
  def swap(self, nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
    
  def reverse(self, nums, start, end):
    while start < end:
      self.swap(nums, start, end)
      start += 1
      break
    
    
  def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Step 1: Find the first decreasing element from the right
        
        n = len(nums)
        index = -1
        
        for i in range(n-2, -1, -1):
          if nums[i] < nums[i+1]:
            index = i
            break
          
        # Step 2: Find next greater element to swap with nums[index]
        if index != -1:
          for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
              self.swap(nums, i, index)
              break
        
        # Step 3: Reverse the suffix (right part of the array)
        self.reverse(nums, index+1, n-1)