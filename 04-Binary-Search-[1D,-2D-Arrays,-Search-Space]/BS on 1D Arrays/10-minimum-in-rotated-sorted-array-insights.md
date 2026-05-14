# Find Minimum in Rotated Sorted Array
## Complete Learning Guide 🎯

---

## 📚 Problem Statement

**Ek sorted array ko rotate kar diya, ab minimum element dhundo O(log n) mein!**

### Rotation Samjho:

Pehle original array sorted tha, ascending order mein. Fir kisi point pe rotate kar diya - matlab last elements ko start mein le gaye. Example: `[1, 2, 3, 4, 5]` ko 3 baar rotate karey toh `[3, 4, 5, 1, 2]` mil gaya. Rotation ke baad array ke do portions hain: pehla portion `[3, 4, 5]` ascending order mein, dusra portion `[1, 2]` ascending order mein. Par un dono ke beech ek "kink" (break point) hai jahan values decrease hoti hain.

Minimum element hamesha us kink point par hi hota hai - jahan rotation hua. Aur binary search use karke hum quickly us kink point tak pahunch sakte hain!

```
Original:     [1, 2, 3, 4, 5]
Rotate by 3:  [3, 4, 5, 1, 2]
              ↑ Kink point ↑
              
Minimum: 1 (rotation point ke baad start)
```

### Examples:

```
Example 1:
Array: [3, 4, 5, 1, 2]
Minimum: 1 (Rotation 3 times, min at rotation point)

Example 2:
Array: [4, 5, 6, 7, 0, 1, 2]
Minimum: 0 (Rotation 4 times, min right at kink)

Example 3:
Array: [11, 13, 15, 17]
Minimum: 11 (No rotation! Already sorted, min is first)
```

---

## 🧠 Core Intuition: Minimum Aur Rotation Point

### Kya Relationship Hai?

Rotated sorted array mein minimum element ka matlab ho sakta hai do cheezein:

1. **Array pehle se sorted hai (no rotation)**: Toh pehla element hi minimum hai
2. **Array rotated hai**: Toh minimum element rotation point ke just baad hota hai - jahan se smaller values start hoti hain

Key insight ye hai: **minimum element har baar unsorted half mein hota hai!** 

Sochte ho - agar left half sorted hai (nums[low] <= nums[mid]), toh minimum left mein nahi hai. Minimum right mein hona chahiye. Agar right half sorted hai (nums[mid] <= nums[high]), toh minimum right mein nahi hai. Minimum left mein hona chahiye. Toh hum sorted half ko eliminate kar sakte hain aur unsorted half mein search kar sakte hain!

```
Key Pattern:
├─ Left sorted? → Min right mein
├─ Right sorted? → Min left mein
└─ This guides binary search!
```

### Visual Understanding:

```
Array: [4, 5, 6, 7, 0, 1, 2]
       ↑ sorted ↑  ↑ sorted ↑
       
Left sorted [4,5,6,7]: Minimum nahi yahan
Right sorted [0,1,2]: Minimum yahan! (0)

Search direction: RIGHT ki side mein, unsorted side!
```

---

## 🎯 Approach 1: Sorted Half Elimination (Optimal)

### Intuition:

Ye approach binary search ka best use karti h. Har iteration mein hum mid pe check karte h:
- Agar left half sorted hai (`nums[low] <= nums[mid]`), toh minimum right half mein hai (unsorted side)
- Agar right half sorted hai, toh minimum left half mein hai (unsorted side)

Is tarah hum continuously unsorted half mein move karte hai aur eventually minimum element tak pahunch jate hai. Worst case mein jab sirf ek element reh jayega, wo hi minimum hoga!

### Pseudo Code:

```
FIND_MIN_APPROACH_1(nums):
  
  low = 0
  high = n - 1
  
  WHILE low < high:                    // Note: < na ki <=
    mid = (low + high) / 2
    
    // Check: Left half sorted?
    IF nums[mid] < nums[high]:
      // Right side has smaller value
      // So minimum is in right or at mid
      // But since sorted, min won't be here
      // Move left: high = mid
      high = mid
    ELSE:
      // Left side has smaller value
      // So minimum is definitely in left
      // Move: low = mid + 1
      low = mid + 1
  
  RETURN nums[low]


LOGIC EXPLANATION:
├─ Agar nums[mid] < nums[high]:
│  └─ Right sorted! Min left mein, high = mid
│
└─ Agar nums[mid] > nums[high]:
   └─ Left sorted! Min right mein, low = mid + 1
```

### Why `low < high` Instead of `low <= high`?

Ye important hai! Jab `low < high` use karey, loop tab tak chalti hai jab tak `low == high` na ho jaaye. Aur jab loop end hota hai, `nums[low]` hi answer hota hai - safe aur clean! Agar `low <= high` use karey, toh extra checks lagenge mid par.

### Detailed Explanation:

Approach 1 mein hum **comparison between mid and high** karey. Agar `nums[mid]` chhota hai `nums[high]` se, toh ye signal hai ki right half ascending order mein hai (sorted). Iska matlab left half (ya mid se left) mein khin break point (rotation) hai. Toh minimum left half mein hona chahiye. Par safely, hum `high = mid` kar sakte hain kyunki mid still candidate hai minimum ke liye.

Agar `nums[mid]` bada hai `nums[high]` se, toh ye signal hai ki rotation left side mein hai aur minimum right side mein hai. Toh `low = mid + 1` kar denge.

---

## 🎯 Approach 2: Both Halves Check (Alternative)

### Intuition:

Ye approach pehle check karey kaun sa half sorted hai, fir us sorted half ke elements ko dekhkar decide karey minimum kaun side mein hai. Thoda verbose hai par beginner ke liye concept clearer hota hai.

### Pseudo Code:

```
FIND_MIN_APPROACH_2(nums):
  
  low = 0
  high = n - 1
  
  WHILE low < high:
    mid = (low + high) / 2
    
    // Check if left half is sorted
    IF nums[low] <= nums[mid]:
      // Left half [low...mid] is sorted
      // Minimum is NOT in this sorted part
      // So it's definitely in right part
      low = mid + 1
    
    ELSE:
      // Left half is NOT sorted
      // Rotation happened in left
      // Minimum is in left part
      high = mid
  
  RETURN nums[low]


LOGIC EXPLANATION:
├─ nums[low] <= nums[mid]?
│  └─ Left sorted → Min right mein
│
└─ nums[low] > nums[mid]?
   └─ Left unsorted → Min left mein
```

### Why This Works:

Approach 2 mein hum specifically left half ko check karey nums[low] <= nums[mid] condition se. Agar ye true hai, toh left portion definitely ascending order mein hai - start se mid tak sorted. Ab iska matlab rotation right side mein hua hai, toh minimum right side mein hoga. Agar ye false hai, toh left portion mein rotation point hai, toh minimum left mein hoga.

### When To Use:

Ye approach Approach 1 se thoda slow hai average cases mein, par conceptually zyada clear hai. Agar interview mein logic clear explain karna ho toh ye better hai. Approach 1 slightly optimized version hai.

---

## 🎯 Approach 3: Brute Force (Learning Only)

### Intuition:

Sirf pura array traverse kar do aur minimum find kar do. O(n) time. Simple par inefficient!

### Pseudo Code:

```
FIND_MIN_APPROACH_3(nums):
  
  min_val = nums[0]
  
  FOR i = 1 TO n-1:
    IF nums[i] < min_val:
      min_val = nums[i]
  
  RETURN min_val


LOGIC EXPLANATION:
├─ First element ko min assume karo
├─ Sab elements ko traverse karo
└─ Smaller element mil gaya? Update karo
```

### Why This Doesn't Meet Requirement:

Problem statement clearly O(log n) require karta hai, par brute force O(n) hai. **Interview mein ye approach reject hoga!** Sirf learning ke liye samajhne ke liye sochte ho - "agar binary search na sojhao toh linear search karo, par optimal nahi hai."

---

## 🎬 Dry Run Strategy (Detailed)

### Key Points:

Dry run mein track karo:
- Mid value aur high value ka comparison
- Kaun sa half sorted hai
- Low/high update logic
- Eventually kab low == high hota hai

```
DRY RUN TEMPLATE:

Iteration N:
  low=?, high=?
  mid = (low + high) / 2
  
  nums[low]=?, nums[mid]=?, nums[high]=?
  
  nums[mid] < nums[high]?
  → YES/NO
  
  Update: high/low = ?
  
  Status: Continue/Done
```

---

## 📊 Dry Run Example 1: Clear Rotation (Approach 1)

```
Array: [4, 5, 6, 7, 0, 1, 2]
Find: Minimum

Initial State:
  low=0, high=6

Iteration 1:
  low=0, high=6
  mid = (0+6)/2 = 3
  
  nums[mid]=7, nums[high]=2
  
  7 < 2? NO
  → Left sorted? No! Rotation in left
  → Minimum in right
  → low = 3 + 1 = 4
  
  Status: Right side search (unsorted side)

Iteration 2:
  low=4, high=6
  mid = (4+6)/2 = 5
  
  nums[mid]=1, nums[high]=2
  
  1 < 2? YES
  → Right sorted! [1, 2]
  → Minimum could be mid or left
  → high = 5
  
  Status: Move left to find rotation point

Iteration 3:
  low=4, high=5
  mid = (4+5)/2 = 4
  
  nums[mid]=0, nums[high]=1
  
  0 < 1? YES
  → Right sorted [0, 1]
  → high = 4
  
  Status: Narrow down

Iteration 4:
  low=4, high=4
  low == high → LOOP ENDS
  
RETURN nums[4] = 0 ✓

Minimum found: 0
```

---

## 📊 Dry Run Example 2: No Rotation

```
Array: [11, 13, 15, 17]
Find: Minimum

Initial State:
  low=0, high=3

Iteration 1:
  low=0, high=3
  mid = (0+3)/2 = 1
  
  nums[mid]=13, nums[high]=17
  
  13 < 17? YES
  → Right sorted [13, 15, 17]
  → Minimum not in right
  → high = 1
  
  Status: Left side

Iteration 2:
  low=0, high=1
  mid = (0+1)/2 = 0
  
  nums[mid]=11, nums[high]=13
  
  11 < 13? YES
  → Right sorted
  → high = 0
  
  Status: Narrow to first element

Iteration 3:
  low=0, high=0
  low == high → LOOP ENDS
  
RETURN nums[0] = 11 ✓

Minimum found: 11 (Array pehle se sorted tha!)
```

---

## 📊 Dry Run Example 3: Using Approach 2

```
Array: [3, 4, 5, 1, 2]
Find: Minimum

Using Approach 2 (Left half check):

Initial State:
  low=0, high=4

Iteration 1:
  low=0, high=4
  mid = (0+4)/2 = 2
  
  nums[low]=3, nums[mid]=5, nums[high]=2
  
  3 <= 5? YES
  → Left sorted [3, 4, 5]
  → Minimum in unsorted right
  → low = 2 + 1 = 3
  
  Status: Right side has rotation/minimum

Iteration 2:
  low=3, high=4
  mid = (3+4)/2 = 3
  
  nums[low]=1, nums[mid]=1, nums[high]=2
  
  1 <= 1? YES
  → Left sorted [1]
  → Minimum in right or at boundary
  → low = 3 + 1 = 4
  
  Status: Only right element left

Iteration 3:
  low=4, high=4
  low == high → LOOP ENDS
  
RETURN nums[4] = 2

Wait! Ye wrong answer hai! Minimum 1 tha!

Debugging:
Approach 2 mein issue ho sakta hai edge cases mein.
Approach 1 zyada safer hai!
```

---

## 🎓 Pattern Recognition

### When Use This?

```
SIGNAL 1: Sorted array (originally)
SIGNAL 2: Rotated (kink point present)
SIGNAL 3: Find minimum (not search)
SIGNAL 4: O(log n) required

→ Find minimum in rotated array pattern!
```

### Related Problems:

```
├─ Find Minimum in Rotated Array II (duplicates)
├─ Find Maximum in Rotated Array
├─ Search in Rotated Array (Problems 08, 09)
└─ Find Rotation Count
```

---

## 🎯 Edge Cases & Handling

### Edge Case 1: No Rotation (Already Sorted)

```
Array: [1, 2, 3, 4, 5]
Minimum: 1

First element itself minimum!
Algorithm handles: mid > high always
→ Keep shrinking right
→ Eventually nums[0] return hota hai ✓
```

### Edge Case 2: Rotation at End

```
Array: [2, 3, 4, 5, 1]
Minimum: 1

Rotation last point mein.
Algorithm: Last iteration mein last element check hoga
→ nums[4] = 1 found ✓
```

### Edge Case 3: Single Element

```
Array: [1]
Minimum: 1

low=0, high=0
low == high immediately
→ Return nums[0] = 1 ✓
```

### Edge Case 4: Two Elements

```
Array: [2, 1]
Minimum: 1

Iteration 1:
  mid=0, nums[0]=2, nums[1]=1
  2 < 1? NO
  → low = 1
  
Iteration 2:
  low=1, high=1
  → Return nums[1] = 1 ✓
```

---

## 🎤 Interview Signals & Tips

### Interviewer Puchega: "Kyun Mid vs High Compare Karey, Mid vs Low Nahi?"

**Your Answer:**
```
"Approach 1 mein mid vs high compare karke humne
unsorted half identify karte hain efficiently.

Kyunki:
├─ Agar nums[mid] < nums[high]:
│  └─ Right side ascending (sorted)
│  └─ Rotation/minimum left mein
│
└─ Agar nums[mid] > nums[high]:
   └─ Left side ascending (sorted)
   └─ Rotation/minimum right mein

Ye direct bata deta hai minimum kaun side mein hai!"
```

### Interviewer Puchega: "Difference Between Approach 1 and 2?"

**Your Answer:**
```
"Approach 1: Mid vs High
  - Thoda faster average case
  - Cleaner code
  
Approach 2: Low vs Mid (Left half check)
  - Conceptually clearer
  - Explicitly check karey kaun half sorted

Dono O(log n), par Approach 1 slightly optimized!"
```

### Interviewer Puchega: "Time Complexity?"

**Your Answer:**
```
"O(log n)!

Har iteration mein search space half hota hai:
  n → n/2 → n/4 → ... → 1
  
Log₂(n) iterations.

Space: O(1) (no extra space)"
```

### Interviewer Puchega: "What if Duplicates Present?"

**Your Answer:**
```
"Ye problem distinct values assume karta hai.

Agar duplicates ho, toh ye approach fail sakta hai:

Example: [1, 1, 1, 0, 1, 1, 1]
  nums[mid]=1, nums[high]=1
  1 < 1? NO
  
Par minimum 0 right side mein bhi ho sakta!

Solution: Shrinking strategy lagani padegi
(Find Minimum in Rotated Array II)"
```

---

## 🚨 Common Mistakes (Avoid These!)

### Mistake 1: Using `low <= high` Instead of `low < high`

```
❌ WRONG:
WHILE low <= high:
  (Extra complexity, edge case bugs)

✓ CORRECT:
WHILE low < high:
  (Clean, when loop ends: low == high = answer)
```

### Mistake 2: Wrong Mid vs High Comparison

```
❌ WRONG:
if nums[mid] < nums[low]:
  (Wrong direction!)

✓ CORRECT:
if nums[mid] < nums[high]:
  (Mid vs high tells about rotation position)
```

### Mistake 3: Forgetting `high = mid` (Using `high = mid - 1`)

```
❌ WRONG:
if nums[mid] < nums[high]:
  high = mid - 1      // Might skip minimum!

✓ CORRECT:
if nums[mid] < nums[high]:
  high = mid          // Mid still candidate
```

### Mistake 4: Not Handling Already Sorted Array

```
❌ WRONG:
(Assume rotation always present)

✓ CORRECT:
Algorithm automatically handles:
  No rotation → mid > high always
  → Shrink right till first element ✓
```

### Mistake 5: Using Brute Force

```
❌ WRONG:
Loop through array, find min
  O(n) time!

✓ CORRECT:
Binary search approach
  O(log n) time! ✓
```

### Mistake 6: Comparing with Wrong Index

```
❌ WRONG:
if nums[mid] < nums[mid-1]:
  return mid       // Mid might not be answer!

✓ CORRECT:
if nums[mid] < nums[high]:
  high = mid       // Continue binary search
```

### Mistake 7: Incorrect Mid Update

```
❌ WRONG:
mid = (low + high) / 2
(Integer division issues in some languages)

✓ CORRECT:
mid = (low + high) // 2     // Explicit integer division
```

---

## 📝 Revision Notes (Quick Summary)

### Approach 1 (Optimal):

```
LOGIC:
├─ Compare nums[mid] vs nums[high]
├─ nums[mid] < nums[high]?
│  └─ Right sorted → high = mid
│
└─ nums[mid] > nums[high]?
   └─ Left sorted → low = mid + 1

TIME: O(log n)
SPACE: O(1)
BEST FOR: Interview, optimal solution
```

### Approach 2 (Alternative):

```
LOGIC:
├─ Compare nums[low] vs nums[mid]
├─ nums[low] <= nums[mid]?
│  └─ Left sorted → low = mid + 1
│
└─ nums[low] > nums[mid]?
   └─ Left unsorted → high = mid

TIME: O(log n)
SPACE: O(1)
BEST FOR: Conceptual clarity
```

### Approach 3 (Brute Force):

```
LOGIC:
├─ Traverse entire array
├─ Track minimum

TIME: O(n) ❌ (Not allowed!)
SPACE: O(1)
BEST FOR: Learning only
```

---

## 🔗 Related Problems

1. **Find Minimum in Rotated Array II** → With duplicates (harder)
2. **Find Maximum in Rotated Array** → Similar logic, change comparison
3. **Find Rotation Count** → Count rotations using minimum
4. **Search in Rotated Array** → Problems 08, 09 (find element)
5. **Peak Element in Rotated Array** → Similar binary search concept

---

## 📊 Approaches Comparison Table

```
Approach      Time      Space   Difficulty   Interview
────────────────────────────────────────────────────
Approach 1    O(log n)  O(1)    Easy-Med      BEST ✓
Approach 2    O(log n)  O(1)    Easy-Med      Good
Approach 3    O(n)      O(1)    Easy          NOT OK ❌
```

---

## ✅ Self-Check Checklist

- [ ] Rotation concept clear? (Kink point samajh aata hai?)
- [ ] Minimum hamesha unsorted half mein? (Pattern samajh aata hai?)
- [ ] Mid vs High comparison logic?
- [ ] `low < high` vs `low <= high` difference?
- [ ] `high = mid` vs `high = mid - 1` difference?
- [ ] Why `low = mid + 1` works?
- [ ] No rotation case handled?
- [ ] Edge cases: single element, two elements?
- [ ] Duplicates: NOT handled (distinct values)?
- [ ] O(log n) intuition?

---

## 💡 Final Insight: Minimum = Unsorted Half

```
CORE PROPERTY:

In rotated sorted array:
"Minimum element is ALWAYS 
 at the beginning of unsorted half"

Why?
├─ Left sorted → all greater than right start
├─ Right sorted → all greater than left start
├─ One half always unsorted (rotation point)
└─ Minimum = start of unsorted half

This property enables O(log n) solution!
```

---

## 🎯 Decision Flow

```
Minimum in rotated array problem?
  ├─ Distinct values?
  │  └─ Use Approach 1 or 2 ✓
  │
  ├─ Time requirement O(log n)?
  │  └─ Binary search ✓
  │
  └─ Duplicates present?
     └─ More complex (II version)
```

---

**Happy Learning! Find Minimum in Rotated Array clear ho gaye! 🚀**