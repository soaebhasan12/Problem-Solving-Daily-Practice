# Search in rotated sorted array-II

"""
Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.


Example 1
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Output: True
Explanation: The element 3 is present in the array. So, the answer is True.

Example 2
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Output: False
Explanation:The element 10 is not present in the array. So, the answer is False.
"""

class Solution:
    def search(self, nums, target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1
        
        while low <= high:
            
            # SHRINK: Remove ambiguity
            while low < high and nums[low] == nums[high]:
                high -= 1                  # ← Shrink from right
            
            mid = (low + high) // 2
            
            # Step 1: Exact match?
            if nums[mid] == target:
                return True
            
            # Step 2: Left half sorted?
            if nums[low] <= nums[mid]:
                # Target in left half?
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1        # LEFT search
                else:
                    low = mid + 1         # RIGHT search
                
            # Step 3: Right half sorted (else)
            else:
                # Target in right half?
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1         # RIGHT search
                else:
                    high = mid - 1        # LEFT search
        
        return False              # Not found