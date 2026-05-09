# Count Occurrences in a Sorted Array

"""
You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.

Return the count of occurrences of target in the array.

Example 1
Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1
Output: 3
Explanation: The number 1 appears 3 times in the array.

Example 2
Input: arr = [5, 5, 5, 5, 5, 5], target = 5
Output: 6
Explanation: All elements in the array are 5, so the target appears 6 times.
"""


class Solution:
      
    def firstOccurence(self, arr, target):
      
      low = 0
      high = len(arr) - 1
      
      first = -1

      while low <= high:
        
        mid = ( low + high ) // 2
        
        if arr[mid] == target:
          first = mid
          high = mid - 1
        
        elif arr[mid] < target:
          low = mid + 1
        
        else:
          high = mid - 1
          
      return first
      
    
    def lastOccurence(self, arr, target):
      
      low = 0
      high = len(arr) - 1
      
      last = -1
      
      while low <= high:
        mid = ( low + high ) // 2
        
        if arr[mid] == target:
          last = mid
          low = mid + 1
            
        elif arr[mid] < target:
          low = mid + 1
                  
        else:
          high = mid - 1
      
      return last
      
    
    
    def countOccurrences(self, arr, target):
      first = self.firstOccurence(arr, target)
      
      if first == -1:
        return [-1, -1]
      
      last = self.lastOccurence(arr, target)
      
      print((last - first) + 1)
      
obj = Solution()
# obj.countOccurrences(arr = [5, 5, 5, 5, 5, 5], target = 5)        # OUTPUT: 6
obj.countOccurrences(arr=[0, 0, 1, 1, 1, 2, 3], target=1)           # OUTPUT: 3