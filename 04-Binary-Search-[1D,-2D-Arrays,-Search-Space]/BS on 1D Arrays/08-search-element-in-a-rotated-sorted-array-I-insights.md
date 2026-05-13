# Search in Rotated Sorted Array
## Complete Learning Guide (Hinglish) 🎯

---

## 📚 Problem Statement (Hindi mein)

**Sorted array ko left rotate kar diya, fir target dhundo!**

### Rotation Samjho:

```
Original:     [0, 1, 2, 4, 5, 6, 7]
Rotate by 3:  [4, 5, 6, 7, 0, 1, 2]
              ↑ Index 3 se start ↑

Key Point:
- Array sorted tha, par ab rotated hai
- Ek kink/pivot hota hai jahan break hota hai
- Target dhundo O(log n) mein!
```

### Examples:

```
Example 1:
Array: [4, 5, 6, 7, 0, 1, 2]
Target: 0
Output: 4 (index jahan 0 hai)

---

Example 2:
Array: [4, 5, 6, 7, 0, 1, 2]
Target: 3
Output: -1 (3 nahi hai)

---

Example 3:
Array: [1]
Target: 0
Output: -1 (0 nahi hai)
```

---

## 🧠 Core Intuition: Rotation aur Half Sorting

### Problem Ko Samjho:

```
Normal Sorted Array:
  [1, 2, 3, 4, 5, 6, 7]
  Simple binary search ✓

Rotated Array:
  [4, 5, 6, 7, 0, 1, 2]
         ↑
      Kink/Pivot
      
Challenges:
├─ Array fully sorted nahi
├─ Ek part ascending, dusra ascending (par overlap hai)
└─ Target kaunse side mein hai?

Solution:
├─ Har iteration mein ONE half zaroor sorted hai!
├─ Check: Target sorted half mein hai ya nahi?
├─ Based on answer: Search direction decide kro
└─ Continue until target mil jaye
```

### Key Insight: One Half Always Sorted

```
Rotated Array mein, agar tum mid pe sahi ho gaye:

Case 1: Left half sorted
        Right half unsorted
        
        [4, 5, 6, | 7, 0, 1, 2]
         ↑ sorted ↑

Case 2: Right half sorted
        Left half unsorted
        
        [4, 5, 6, 7, | 0, 1, 2]
                     ↑ sorted ↑

RULE: LOW se MID tak sorted? → Left sorted
      MID se HIGH tak sorted? → Right sorted
```

---

## 🎯 Concept: Sorted Half Detection

### Left Half Sorted (nums[low] <= nums[mid])

```
Definition:
"Left half pehle se low tak sorted hai"

Detection:
  if nums[low] <= nums[mid]:
    → Left half sorted hai!

Example:
  Array: [4, 5, 6, 7, 0, 1, 2]
  low=0, mid=3
  nums[0]=4, nums[3]=7
  
  4 <= 7? YES
  → Left half [4,5,6,7] sorted hai ✓

Visual:
  [4, 5, 6, 7 | 0, 1, 2]
   ↑ sorted ↑
   
Check: 4 <= 7? YES (start <= end)
```

### Right Half Sorted (nums[mid] <= nums[high])

```
Definition:
"Right half mid se high tak sorted hai"

Detection:
  if nums[mid] <= nums[high]:
    → Right half sorted hai!

Example:
  Array: [4, 5, 6, 7, 0, 1, 2]
  mid=4, high=6
  nums[4]=0, nums[6]=2
  
  0 <= 2? YES
  → Right half [0,1,2] sorted hai ✓

Visual:
  [4, 5, 6, 7 | 0, 1, 2]
              ↑ sorted ↑
              
Check: 0 <= 2? YES (start <= end)
```

---

## 🔍 Algorithm: Condition Checking Strategy

### Step 1: Mid == Target?

```
IMMEDIATE CHECK:
if nums[mid] == target:
  return mid

(Mil gaya, khush ho jao!)
```

### Step 2: Left Half Sorted?

```
if nums[low] <= nums[mid]:
  → Left half sorted
  
  NEXT: Target left mein hai ya nahi?
  if nums[low] <= target <= nums[mid]:
    → Target left mein hai!
    → high = mid - 1 (left mein search karo)
  else:
    → Target right mein hai
    → low = mid + 1 (right mein search karo)
```

### Step 3: Right Half Sorted

```
else:  (iska matlab left unsorted, right sorted!)
  → Right half sorted
  
  NEXT: Target right mein hai ya nahi?
  if nums[mid] <= target <= nums[high]:
    → Target right mein hai!
    → low = mid + 1 (right mein search karo)
  else:
    → Target left mein hai
    → high = mid - 1 (left mein search karo)
```

---

## 📝 Pseudo Code (Step-by-Step)

### Main Algorithm

```
SEARCH_ROTATED(nums, target):
  
  low = 0
  high = n - 1
  
  WHILE low <= high:
    mid = (low + high) / 2
    
    // Step 1: Exact match?
    IF nums[mid] == target:
      RETURN mid
    
    // Step 2: Left half sorted?
    IF nums[low] <= nums[mid]:
      
      // Target left half mein?
      IF nums[low] <= target AND target <= nums[mid]:
        high = mid - 1    // LEFT search
      ELSE:
        low = mid + 1     // RIGHT search
    
    // Step 3: Right half sorted (else)
    ELSE:
      
      // Target right half mein?
      IF nums[mid] <= target AND target <= nums[high]:
        low = mid + 1     // RIGHT search
      ELSE:
        high = mid - 1    // LEFT search
  
  RETURN -1  // Not found


LOGIC FLOW:
├─ Find mid
├─ Mid == target? Return
├─ Identify: Kaun sa half sorted?
├─ Check: Target us sorted half mein?
├─ Update: low/high accordingly
└─ Repeat until found or exhausted
```

### Decision Tree (Visual)

```
                    Array[low...high]
                           |
                        mid = ?
                           |
                   Is nums[mid]==target?
                    /              \
                  YES              NO
                   |                |
                RETURN          Kaun half sorted?
                mid             /            \
                           LEFT            RIGHT
                           |                |
                    Target in     Target in
                    LEFT half?    RIGHT half?
                    /     \       /      \
                  YES    NO    YES      NO
                   |      |      |       |
                 high=  low=  low=   high=
                mid-1  mid+1  mid+1  mid-1
```

---

## 🎬 Dry Run Strategy (Detailed)

### Key Points:

```
DRY RUN MEIN TRACK KARO:
├─ Mid value aur target comparison
├─ Sorted half identification
├─ Target vs sorted half boundaries
├─ low/high update reasoning
└─ Iteration after iteration

Confusion avoid karey:
"Ye left sorted hai, toh target left mein hai?"
No! Target sorted half OUTSIDE bhi ho sakta!
```

---

## 📊 Dry Run Example 1: Target Mil Gaya (Left Sorted)

```
Array: [4, 5, 6, 7, 0, 1, 2]
Target: 5

Initial State:
  low=0, high=6
  Find: 5

Iteration 1:
  low=0, high=6
  mid = (0+6)/2 = 3
  nums[3] = 7
  
  7 == 5? NO
  
  nums[low]=4, nums[mid]=7
  4 <= 7? YES
  → LEFT HALF SORTED [4,5,6,7]
  
  Target in left half?
  nums[low] <= target <= nums[mid]?
  4 <= 5 <= 7? YES ✓
  → high = 3 - 1 = 2
  
  Status: Target left mein, search left

|---|---|---|---|---|---|---|
| 4 | 5 | 6 | 7 | 0 | 1 | 2 |
  0   1   2  [3] 4   5   6
              ↑
            mid
            
            Target 5 left mein (4 to 7)

Iteration 2:
  low=0, high=2
  mid = (0+2)/2 = 1
  nums[1] = 5
  
  5 == 5? YES ✓
  → RETURN 1 ✓

Output: Index 1 ✓
```

---

## 📊 Dry Run Example 2: Target Right Sorted Half Mein

```
Array: [4, 5, 6, 7, 0, 1, 2]
Target: 0

Initial State:
  low=0, high=6
  Find: 0

Iteration 1:
  low=0, high=6
  mid = (0+6)/2 = 3
  nums[3] = 7
  
  7 == 0? NO
  
  nums[low]=4, nums[mid]=7
  4 <= 7? YES
  → LEFT HALF SORTED [4,5,6,7]
  
  Target in left half?
  4 <= 0 <= 7? NO ❌
  → Target RIGHT mein!
  → low = 3 + 1 = 4
  
  Status: Target right mein, search right

|---|---|---|---|---|---|---|
| 4 | 5 | 6 | 7 | 0 | 1 | 2 |
  0   1   2   3  [4] 5   6
                  ↑
                Move here

Iteration 2:
  low=4, high=6
  mid = (4+6)/2 = 5
  nums[5] = 1
  
  1 == 0? NO
  
  nums[low]=0, nums[mid]=1
  0 <= 1? YES
  → RIGHT HALF SORTED [0,1,2]
  
  Target in right half?
  1 <= 0 <= 2? NO ❌
  → Target LEFT mein (relative to mid)
  → high = 5 - 1 = 4
  
  Status: Recalibrate

|---|---|---|---|---|---|---|
| 4 | 5 | 6 | 7 | 0 | 1 | 2 |
  0   1   2   3  [4] 5   6
                  ↑
                High move here

Iteration 3:
  low=4, high=4
  mid = (4+4)/2 = 4
  nums[4] = 0
  
  0 == 0? YES ✓
  → RETURN 4 ✓

Output: Index 4 ✓
```

---

## 📊 Dry Run Example 3: Target Nahi Hai

```
Array: [4, 5, 6, 7, 0, 1, 2]
Target: 3

Initial State:
  low=0, high=6
  Find: 3

Iteration 1:
  low=0, high=6
  mid=3, nums[3]=7
  
  7==3? NO
  4<=7? YES → LEFT SORTED [4,5,6,7]
  4<=3<=7? NO → RIGHT mein
  low=4

Iteration 2:
  low=4, high=6
  mid=5, nums[5]=1
  
  1==3? NO
  0<=1? YES → RIGHT SORTED [0,1,2]
  1<=3<=2? NO → LEFT mein (relative)
  high=4

Iteration 3:
  low=4, high=4
  mid=4, nums[4]=0
  
  0==3? NO
  0<=0? YES → RIGHT SORTED
  0<=3<=2? NO → LEFT mein
  high=3

Iteration 4:
  low=4, high=3
  low > high → LOOP ENDS
  
RETURN -1 ✓ (Not found)
```

---

## 📊 Dry Run Example 4: Right Half Sorted

```
Array: [5, 6, 7, 0, 1, 2, 3]
Target: 1

Initial State:
  low=0, high=6
  Find: 1

Iteration 1:
  low=0, high=6
  mid=3, nums[3]=0
  
  0==1? NO
  5<=0? NO ❌
  → RIGHT HALF SORTED [0,1,2,3]
  
  Target in right half?
  0<=1<=3? YES ✓
  → low=4 (RIGHT search)

|---|---|---|---|---|---|---|
| 5 | 6 | 7 | 0 | 1 | 2 | 3 |
  0   1   2   3  [4] 5   6

Iteration 2:
  low=4, high=6
  mid=5, nums[5]=2
  
  2==1? NO
  0<=2? YES → RIGHT SORTED
  0<=1<=3? YES
  → low=6

Iteration 3:
  low=6, high=6
  mid=6, nums[6]=3
  
  3==1? NO
  1<=3? YES → RIGHT SORTED
  2<=1<=3? NO (2 > 1!)
  → high=5

Iteration 4:
  low=6, high=5
  low > high → LOOP ENDS
  
RETURN -1

Wait! 1 array mein hai par nahi mila? 
Let me recheck dry run...

Actually, mistake tha. Let me redo:

Iteration 2:
  low=4, high=6
  mid=5, nums[5]=2
  
  2==1? NO
  nums[low]=1, nums[mid]=2
  1<=2? YES → RIGHT SORTED [1,2,3]
  
  1<=1<=3? YES
  → Continue RIGHT
  → low=6

Iteration 3:
  low=6, high=6
  mid=6, nums[6]=3
  
  3==1? NO
  nums[low]=3, nums[mid]=3
  3<=3? YES (but this is edge case)
  → Rotation point, only one element
  
  1<=1<=3? NO (nums[low]=3 != 1)
  high=5

Iteration 4:
  low=6, high=5
  low > high → LOOP ENDS
  
Actually, better approach:

Iteration 2:
  low=4, high=6
  mid=5, nums[5]=2
  
  2==1? NO
  nums[low]=1, nums[mid]=2
  1<=2? YES → RIGHT SORTED [1,2,3]
  
  Target 1 in [1,2,3]?
  1<=1<=3? YES
  → low=6

Iteration 3:
  low=6, high=6
  mid=6, nums[6]=3
  
  3==1? NO
  3<=3? YES (single element, trivially sorted)
  1<=1<=3? NO (nums[low]=3)
  high=5

Wait, nums[low] should be nums[6]=3...

Let me trace more carefully:

Iteration 3:
  low=6, high=6
  mid = (6+6)/2 = 6
  nums[6] = 3
  
  3==1? NO
  
  nums[low]=nums[6]=3
  nums[mid]=nums[6]=3
  
  3<=3? YES → "Right sorted" (trivially)
  
  Target in right half?
  3<=1<=3? NO (1 < 3)
  → Target LEFT
  → high = 6-1 = 5

Iteration 4:
  low=6, high=5
  low > high → LOOP ENDS
  
RETURN -1

(But 1 array mein hai! Array mein check karo:
 [5,6,7,0,1,2,3]
  Index 4 par 1 hai!)
  
Mistake: Logic galat trace kiya.
Let me redo from Iteration 1:

---

CORRECTED TRACE:

Array: [5, 6, 7, 0, 1, 2, 3]
Index:  0  1  2  3  4  5  6
Target: 1

Iteration 1:
  low=0, high=6
  mid = 3
  nums[3] = 0
  
  0==1? NO
  
  nums[low]=5, nums[mid]=0
  5<=0? NO ❌
  → RIGHT HALF SORTED!
  
  nums[mid]=0, nums[high]=3
  0<=3? YES ✓ (Confirmed: Right sorted [0,1,2,3])
  
  Target in right half?
  0<=1<=3? YES ✓
  → low = mid + 1 = 4

Iteration 2:
  low=4, high=6
  mid = 5
  nums[5] = 2
  
  2==1? NO
  
  nums[low]=1, nums[mid]=2
  1<=2? YES ✓
  → LEFT HALF SORTED [1,2]? 
     (In context of this sub-array)
  
  Target in left half [1,2]?
  1<=1<=2? YES ✓
  → high = mid - 1 = 4

Iteration 3:
  low=4, high=4
  mid = 4
  nums[4] = 1
  
  1==1? YES ✓
  → RETURN 4 ✓

Output: Index 4 ✓
```

---

## 🎓 Pattern Recognition

### When Apply This Algorithm?

```
SIGNAL 1: Sorted array (originally)
SIGNAL 2: Array ROTATED (ek kink hai)
SIGNAL 3: Find element
SIGNAL 4: O(log n) required

→ Binary search on rotated array!
```

### Key Patterns:

```
Pattern 1: One half always sorted
  → Use ye property decide karne mein

Pattern 2: Check target in sorted half
  → nums[a] <= target <= nums[b]?
  → Simple boundary check

Pattern 3: Else other half search
  → One half sorted nahi, exclude karo
  → Dusra half mein target zaroori hai
```

### Related Problem Types:

```
1. Search in Rotated Array (Distinct) ← Ye problem
2. Search in Rotated Array II (Duplicates) → Thoda hard
3. Find Minimum in Rotated Array → Similar logic
4. Find Peak Element → Conditional BS
```

---

## 🎯 Edge Cases & Handling

### Edge Case 1: Single Element

```
Array: [1]
Target: 1
Output: 0

Array: [1]
Target: 0
Output: -1

Trace:
  low=0, high=0
  mid=0, nums[0]=1
  
  1==1? YES → RETURN 0 ✓
  1==0? NO → RETURN -1 ✓
```

### Edge Case 2: No Rotation (Already Sorted)

```
Array: [1, 2, 3, 4, 5]
Target: 3

Trace:
  Iteration 1: mid=2, nums[2]=3==3? YES → RETURN 2 ✓
  
(Works perfectly! Algorithm handles no-rotation too)
```

### Edge Case 3: Target First Element

```
Array: [3, 4, 5, 1, 2]
Target: 3

Iteration 1:
  mid=2, nums[2]=5
  5==3? NO
  
  3<=5? YES → LEFT SORTED
  3<=3<=5? YES → high=1

Iteration 2:
  mid=0, nums[0]=3
  3==3? YES → RETURN 0 ✓
```

### Edge Case 4: Target Last Element

```
Array: [3, 4, 5, 1, 2]
Target: 2

Iteration 1:
  mid=2, nums[2]=5
  5==2? NO
  
  3<=5? YES → LEFT SORTED
  3<=2<=5? NO → low=3

Iteration 2:
  mid=4, nums[4]=2
  2==2? YES → RETURN 4 ✓
```

### Edge Case 5: All Same (Edge)

```
Array: [1, 1, 1, 1]
Target: 1

Iteration 1:
  mid=1, nums[1]=1
  1==1? YES → RETURN 1 ✓

(Works, though not true rotation)
```

### Edge Case 6: Target Between Rotation Point

```
Array: [4, 5, 6, 7, 0, 1, 2]
Target: 3

(Already covered in dry run example 3)
Output: -1 ✓
```

---

## 🎤 Interview Signals & Tips

### Interviewer Puchega: "Rotation Kabhi Check Karey?"

**Your Answer:**
```
"Rotation explicitly check nahi karna!

Ye algorithm rotation point find nahi karta.
Instead:

Har iteration mein:
├─ Check: Left half sorted?
├─ Check: Right half sorted?
└─ Based on answer: Search direction

One half always sorted hona zaruri hai!
Rotation ka concept sirf ye ensure karey hai."
```

### Interviewer Puchega: "Kyun nums[low] <= nums[mid]?"

**Your Answer:**
```
"Ye check karey:
'Nums[low] se nums[mid] tak elements
 sorted order mein hain ya nahi?'

Agar YES:
  └─ LEFT HALF SORTED

Agar NO (nums[low] > nums[mid]):
  └─ Kink/Rotation is in left half
  └─ RIGHT HALF MUST BE SORTED

Ye either-or logic binary search ko guide karey!"
```

### Interviewer Puchega: "Kya Duplicates Handle Karey?"

**Your Answer:**
```
"Nahi! Yeh algorithm assumes DISTINCT values.

Duplicates ke saath:
├─ nums[low] == nums[mid]
├─ Or nums[mid] == nums[high]
└─ Can't determine sorted half clearly!

Example: [1, 3, 1, 1, 1]
  mid pe 1, low pe 1
  Left sorted? Can't tell!
  
Duplicates ke liye different approach:
  → Shrink search space
  → low++, high--
  (Search in Rotated Array II)"
```

### Interviewer Puchega: "Time Complexity?"

**Your Answer:**
```
"O(log n)!

Kyunki:
├─ Har iteration mein search space half hota hai
├─ log₂(n) iterations maximum
└─ Each iteration: O(1) comparisons

Space: O(1) (recursion nahi, sirf loop)"
```

### Interviewer Puchega: "Modification: Ye karo"

**Common Modifications:**
```
1. Find minimum element → Similar logic, track min
2. Find rotation point → Find peak/valley
3. Count occurrences → Lower + Upper bound
4. Handle duplicates → Add left++, high-- logic
```

---

## 🚨 Common Mistakes (Avoid These!)

### Mistake 1: Checking Wrong Condition for Sorted Half

```
❌ WRONG:
if nums[mid] <= nums[high]:
  → Left sorted?    (NO! This checks right!)

✓ CORRECT:
if nums[low] <= nums[mid]:
  → Left sorted? (YES! Start to mid)
else:
  → Right sorted (nums[mid] <= nums[high])
```

### Mistake 2: Target Range Check Order

```
❌ WRONG:
if target <= nums[low] AND target <= nums[mid]:
  (Wrong boundaries!)

✓ CORRECT:
if nums[low] <= target AND target <= nums[mid]:
  (Inclusive range check)
```

### Mistake 3: Updating low/high in Wrong Direction

```
❌ WRONG:
if "left half sorted and target in left":
  low = mid + 1     (RIGHT! But target LEFT mein!)

✓ CORRECT:
if "left half sorted and target in left":
  high = mid - 1    (LEFT! Target left mein)
```

### Mistake 4: Forgetting Exact Match Check

```
❌ WRONG:
WHILE low <= high:
  mid = ...
  if nums[low] <= nums[mid]:
    ... (straight to half check)

✓ CORRECT:
WHILE low <= high:
  mid = ...
  if nums[mid] == target:      // First!
    return mid
  if nums[low] <= nums[mid]:
    ... (then half check)
```

### Mistake 5: Assuming Both Halves Unsorted

```
❌ WRONG:
"Agar left unsorted, right bhi unsorted ho sakta!"
(Binary search breaks!)

✓ CORRECT:
"Agar left unsorted, right MUST be sorted!"
(One half always sorted - rotation property)
```

### Mistake 6: Not Handling Edge Case: low == mid == high

```
❌ WRONG:
(Skip the edge case)

✓ CORRECT:
Single element pe:
  if nums[mid] == target: return mid
  else: return -1
  
(Automatically handled by algorithm)
```

### Mistake 7: Complex Conditions

```
❌ WRONG:
if (nums[low] <= nums[mid] AND 
    (target < nums[mid] OR target > nums[high])):
  ...
(Too complex, bug-prone!)

✓ CORRECT:
if nums[low] <= nums[mid]:      // Left sorted?
  if nums[low] <= target <= nums[mid]:
    high = mid - 1
  else:
    low = mid + 1
else:                            // Right sorted
  if nums[mid] <= target <= nums[high]:
    low = mid + 1
  else:
    high = mid - 1
```

### Mistake 8: Forgetting Rotation Point May Be At Different Positions

```
❌ WRONG:
"Rotation pehla hi half mein hai"
(Not always true!)

✓ CORRECT:
"Rotation kahein bhi ho sakta.
 Algorithm target dhoondhe, rotation nahi!"
```

---

## 📝 Revision Notes (Quick Summary)

### Algorithm Overview

```
CORE LOGIC:
├─ Mid == Target? Return
├─ Left half sorted?
│  ├─ Target in left? Search left
│  └─ Else search right
└─ Right half sorted (else)
   ├─ Target in right? Search right
   └─ Else search left

KEY: One half ALWAYS sorted (rotation property)
```

### Sorted Half Check

```
LEFT SORTED:
  Condition: nums[low] <= nums[mid]
  Meaning: Start to mid is ascending
  Range check: nums[low] <= target <= nums[mid]

RIGHT SORTED:
  Condition: nums[mid] <= nums[high] (implicit else)
  Meaning: Mid to end is ascending
  Range check: nums[mid] <= target <= nums[high]
```

### Binary Search Template

```
TEMPLATE:
  low = 0, high = n-1
  
  WHILE low <= high:
    mid = (low + high) / 2
    
    IF EXACT_MATCH:
      return mid
    
    IF HALF_CHECK_A:
      if TARGET_IN_A:
        UPDATE_A
      else:
        UPDATE_B
    ELSE:
      if TARGET_IN_B:
        UPDATE_B
      else:
        UPDATE_A
  
  return -1
```

---

## 🔗 Related Problems

1. **Search in Rotated Array II** → Duplicates handling
2. **Find Minimum in Rotated Array** → Similar sorted-half logic
3. **Rotate Array** → Understanding rotation concept
4. **Find Peak Element** → Conditional binary search
5. **Find the Rotation Count** → Count rotation point

---

## 📊 Key Differences: Normal vs Rotated

```
                Normal BS        Rotated BS
              ────────────      ────────────
Array          Fully sorted     Partially sorted
Check          Direct <, >      Sorted half first
Half Logic     Not needed       Essential!
Complexity     O(log n)         O(log n)
Hardness       Easy             Medium
```

---

## ✅ Self-Check Checklist

- [ ] Rotation concept clear? (Kink in array)
- [ ] One half always sorted? (Rotation property)
- [ ] Left sorted check: nums[low] <= nums[mid]?
- [ ] Target range check: <= target <=?
- [ ] Direction logic: Target in sorted half?
- [ ] Exact match check first?
- [ ] Edge cases: single element, no rotation?
- [ ] Duplicates: NOT handled (distinct values)?
- [ ] Time complexity O(log n)?
- [ ] Dry runs clear?

---

## 🎯 Decision Flow (Interview)

```
Rotated array problem?
  ├─ Duplicates present?
  │  └─ Yes → Search in Rotated Array II (harder)
  │  └─ No → This algorithm ✓
  │
  ├─ What to find?
  │  ├─ Element → Use this algorithm
  │  ├─ Minimum → Slight modification
  │  └─ Peak → Conditional logic
  │
  └─ Time requirement?
     └─ O(log n)? → Binary search ✓
```

---

## 💡 Final Insight: Rotation Property

```
CORE PROPERTY:

In a rotated sorted array:
"At least one half is always sorted"

Why?
├─ Original array: Fully sorted ascending
├─ After rotation: Two sorted parts + pivot
├─ Left of pivot: Ascending
├─ Right of pivot: Ascending
├─ But pivot disconnects them
└─ So: Always one contiguous sorted part

This property is the KEY to O(log n) solution!
```

---

**Happy Learning! Rotated Array Search complete! 🚀**
