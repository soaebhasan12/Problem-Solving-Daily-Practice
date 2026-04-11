# Rearrange array elements by sign

"""
Given an integer array nums of even length consisting of an equal number of positive and negative integers. Return the answer array in such a way that the given conditions are met:


Every consecutive pair of integers have opposite signs.

For all integers with the same sign, the order in which they were present in nums is preserved.

The rearranged array begins with a positive integer.

Example 1
Input : nums = [2, 4, 5, -1, -3, -4]
Output : [2, -1, 4, -3, 5, -4]
Explanation:
The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

Example 2
Input : nums = [1, -1, -3, -4, 2, 3]
Output : [1, -1, 2, -3, 3, -4]
Explanation:
The positive number 1, 2, 3 maintain their relative positions and -1, -3, -4 maintain their relative positions
"""

# APPROACH 1:
nums = [1, -1, -3, -4, 2, 3]

pos = [n for n in nums if n > 0]
neg = [n for n in nums if n < 0]

newNums = []

for i in range(len(pos)):
    newNums.append(pos[i])
    newNums.append(neg[i])

print(newNums)



# APPROACH 2:
nums = [1, -1, -3, -4, 2, 3]

n = len(nums)
newNums = [0] * n

posInd, negInd = 0, 1

for num in nums:
    if num > 0:
        newNums[posInd] = num
        posInd += 2
    else:
        newNums[negInd] = num
        negInd += 2

print(newNums)



# APPROACH 3: (if number of negative and positive elements are not equal)

nums = [1, 2, 3, -1, 1, -1, -3, -4, 2, 3]
# negatives = 5
# positive = 6

res = []

pos = [n for n in nums if n > 0]
neg = [n for n in nums if n < 0]

i, j = 0, 0

while i < len(pos) and j < len(neg):
  res.append(pos[i])
  res.append(neg[j])
  i += 1
  j += 1
  
while i < len(pos):
  res.append(pos[i])
  i += 1
  
while j < len(neg):
  res.append(neg[j])
  j += 1
  
print(res)