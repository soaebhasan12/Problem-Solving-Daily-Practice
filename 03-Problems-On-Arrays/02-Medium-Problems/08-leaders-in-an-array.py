# Leaders in an Array
"""
Given an integer array nums, return a list of all the leaders in the array.

A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

Example 1
Input: nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]

Explanation:
2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

Example 2
Input: nums = [-3, 4, 5, 1, -4, -5]
Output: [5, 1, -4, -5]

Explanation:
-5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]
"""


# BRUTE FORCE APPROACH:
nums = [-3, 4, 5, 1, -4, -5]

ansNums = []

for i in range(len(nums)):
  leader = True
  for j in range(i+1, len(nums)):
    if nums[j] > nums[i]:
      leader = False
      break
  if leader:      # leader == True
    ansNums.append(nums[i])
    
print(ansNums)



# OPTIMAL APPROACH
nums = [-3, 4, 5, 1, -4, -5]
n = len(nums)
ans = []

max_val = float('-inf')

for i in range(n-1, -1, -1):
  if nums[i] > max_val:
    max_val = nums[i]
  else:
    continue
  ans.append(max_val)

ans.reverse()

print(ans)