# Find Peak Element
## Complete Learning Guide (Hinglish) 🎯

---

## 📚 Problem Statement (Hindi mein)

**Array mein peak element dhundo - jo apne neighbors se bada ho!**

### Problem Ko Samjho:

Peak element matlab wo element jo apne immediate neighbors se strictly greater ho. Important point: array ke boundaries ke bahar toh negative infinity samjho. Toh first element aur last element automatically peak ho sakte hain!

Hum multiple peaks ki situation mein kisi bhi ek ko return kar sakte hain. Constraint ye hai: O(log n) time mein solve karna - matlab binary search!

```
Array: [1, 2, 3, 1]
       └─ 3 > 2 aur 3 > 1 ✓
       
Peak at index 2

---

Array: [1, 2, 1, 3, 5, 6, 4]
       └─ 2 > 1 and 2 > 1 ✓
              └─ 5 > 3 and 5 > 6? NO
                     └─ 6 > 5 and 6 > 4 ✓
       
Peaks: Index 1 (value 2) and Index 5 (value 6)
Return any one!
```

### Examples:

```
Example 1:
Array: [1, 2, 3, 1]
Peak: 3 at index 2

Example 2:
Array: [1, 2, 1, 3, 5, 6, 4]
Peak: 2 at index 1, or 6 at index 5

Example 3 (Edge):
Array: [1]
Peak: 1 (boundaries are -∞, so 1 > -∞ ✓)

Example 4 (Edge):
Array: [1, 2]
Peak: 2 (2 > 1 and 2 > -∞ ✓)
```

---

## 🧠 Core Intuition: Slope Aur Direction

### Peak Kaha Hota Hai?

Sochte ho na - agar hum ek point pe khade hain array mein, aur ye point upar jaa raha hai (value increase), toh side mein kahi peak zaroori hai! Kyunki array eventually down aayega (boundaries -∞ hain). 

Key insight: **Jab array increasing ho raha, peak right side mein hai. Jab array decreasing ho raha, peak left side mein hai. Jab ek side bada hai aur ek chhota, wo jo bada side hai, usme peak zaroori hai!**

Toh hum simple check kar sakte hain:
- Agar `nums[mid] < nums[mid+1]` → Right side bada, peak right mein
- Agar `nums[mid] > nums[mid+1]` → Left side bada, peak left mein

Is slope-based logic se hum binary search kar sakte hain!

```
Intuition:

Array: [1, 2, 3, 1]

At index 1 (value 2):
  2 < 3? YES
  → Right side bada!
  → Peak right mein
  → Move RIGHT

At index 2 (value 3):
  3 > 1? YES
  → Left side bada!
  → Peak left side at or before mid
  → Move LEFT or FOUND!
```

### Visual Understanding:

```
Array shape:       /\       ← Peak here!
                  /  \
                 /    \
Value:   1  2  3      1
Index:   0  1  2      3

Increasing side: 1→2→3 (indices 0-2)
Decreasing side: 3→1 (indices 2-3)

Peak at junction: index 2
```

---

## 📝 Pseudo Code (Binary Search)

### Algorithm:

```
FIND_PEAK(nums):
  
  low = 0
  high = n - 1
  
  WHILE low < high:
    mid = (low + high) / 2
    
    // Check: Which side to go?
    IF nums[mid] < nums[mid + 1]:
      // Right side is higher
      // Peak must be on right (increasing direction)
      // Move right: low = mid + 1
      low = mid + 1
    ELSE:
      // Left side is higher or equal
      // Peak is at mid or left
      // Move left: high = mid
      high = mid
  
  RETURN low
  
  (OR return high, dono same hange when loop ends)


LOGIC EXPLANATION:

Slope-based direction:
├─ nums[mid] < nums[mid+1]?
│  └─ Increasing side (→ right)
│  └─ Peak right mein
│  └─ low = mid + 1
│
└─ nums[mid] >= nums[mid+1]?
   └─ Decreasing side (← left)
   └─ Peak left mein or at mid
   └─ high = mid
```

### Why This Works:

Ye algorithm slope detection use karey! Agar mid par value next value se chhoti hai, toh ye signal hai increasing trend - peak ahead mein hai. Agar mid par value next se badi hai, toh decreasing trend - peak behind mein or here hai. Is tarah hum continuously correct direction mein move karey aur eventually peak element tak pahunch jayey.

Guarantee: Peak mil jayega kyunki array ke ends -∞ hain, toh somewhere peak zaroori hoga!

---

## 🎬 Dry Run Strategy (Detailed)

### Key Points:

Dry run mein track karo:
- Mid value aur next value comparison
- Slope detection (increasing/decreasing)
- Low/high update logic
- Eventually kab peak mil jata hai

```
DRY RUN TEMPLATE:

Iteration N:
  low=?, high=?
  mid = (low + high) / 2
  
  nums[mid]=?, nums[mid+1]=?
  
  nums[mid] < nums[mid+1]?
  → YES/NO
  
  Update: low/high = ?
  
  Status: Continue/Done
  
Peak Found At: Index = ?
```

---

## 📊 Dry Run Example 1: Single Peak in Middle

```
Array: [1, 2, 3, 1]
Index:  [0, 1, 2, 3]
Find: Peak element

Initial State:
  low=0, high=3
  Goal: Find index of peak (expected: 2)

Iteration 1:
  low=0, high=3
  mid = (0+3)/2 = 1
  
  nums[mid]=2, nums[mid+1]=3
  
  2 < 3? YES
  → Increasing side!
  → Peak right mein
  → low = 1 + 1 = 2
  
  Status: Move right toward higher values

Iteration 2:
  low=2, high=3
  mid = (2+3)/2 = 2
  
  nums[mid]=3, nums[mid+1]=1
  
  3 < 1? NO
  → Decreasing side!
  → Peak at or left of mid
  → high = mid = 2
  
  Status: Move left to find peak boundary

Iteration 3:
  low=2, high=2
  low < high? 2 < 2? NO
  
  Loop ends!
  
RETURN low = 2 ✓

Peak element: nums[2] = 3
```

---

## 📊 Dry Run Example 2: Multiple Peaks

```
Array: [1, 2, 1, 3, 5, 6, 4]
Index:  [0, 1, 2, 3, 4, 5, 6]
Find: Peak element (any one)

Iteration 1:
  low=0, high=6
  mid = (0+6)/2 = 3
  
  nums[mid]=3, nums[mid+1]=5
  
  3 < 5? YES
  → Peak right mein
  → low = 4
  
  Status: Continue right

Iteration 2:
  low=4, high=6
  mid = (4+6)/2 = 5
  
  nums[mid]=6, nums[mid+1]=4
  
  6 < 4? NO
  → Peak at or left
  → high = 5
  
  Status: Come back left

Iteration 3:
  low=4, high=5
  mid = (4+5)/2 = 4
  
  nums[mid]=5, nums[mid+1]=6
  
  5 < 6? YES
  → Peak right
  → low = 5
  
  Status: Move right again

Iteration 4:
  low=5, high=5
  low < high? NO
  
  Loop ends!
  
RETURN low = 5 ✓

Peak element: nums[5] = 6
(This is one of the peaks; index 1 with value 2 is also valid)
```

---

## 📊 Dry Run Example 3: Peak at Start

```
Array: [3, 2, 1]
Index:  [0, 1, 2]
Find: Peak element

Initial assumption:
  nums[-1] = -∞ (left of array)
  So index 0 mein value 3
  3 > -∞ (left) AND 3 > 2 (right) ✓
  Peak at index 0!

Iteration 1:
  low=0, high=2
  mid = (0+2)/2 = 1
  
  nums[mid]=2, nums[mid+1]=1
  
  2 < 1? NO
  → Peak at or left
  → high = 1
  
  Status: Move left

Iteration 2:
  low=0, high=1
  mid = (0+1)/2 = 0
  
  nums[mid]=3, nums[mid+1]=2
  
  3 < 2? NO
  → Peak at or left
  → high = 0
  
  Status: Narrow to start

Iteration 3:
  low=0, high=0
  low < high? NO
  
  Loop ends!
  
RETURN low = 0 ✓

Peak element: nums[0] = 3 (boundary peak)
```

---

## 📊 Dry Run Example 4: Peak at End

```
Array: [1, 2, 3]
Index:  [0, 1, 2]
Find: Peak element

Initial assumption:
  nums[3] = -∞ (right of array)
  So index 2 mein value 3
  3 > 2 (left) AND 3 > -∞ (right) ✓
  Peak at index 2!

Iteration 1:
  low=0, high=2
  mid = (0+2)/2 = 1
  
  nums[mid]=2, nums[mid+1]=3
  
  2 < 3? YES
  → Peak right mein
  → low = 2
  
  Status: Move right

Iteration 2:
  low=2, high=2
  low < high? NO
  
  Loop ends!
  
RETURN low = 2 ✓

Peak element: nums[2] = 3 (boundary peak)
```

---

## 🎓 Pattern Recognition

### When Use This?

```
SIGNAL 1: Array (sorted or not)
SIGNAL 2: Peak element (local maximum)
SIGNAL 3: Any peak acceptable
SIGNAL 4: O(log n) required

→ Find peak element pattern!
```

### Key Insight: Slope-Based Binary Search

```
Normal binary search: Target comparison
This problem: Slope comparison

Slope logic:
├─ If nums[mid] < nums[mid+1]: Upslope
├─ If nums[mid] > nums[mid+1]: Downslope
└─ Peak is on downslope side!

Universal property: Array mein peak zaroori hoga
(Because boundaries = -∞)
```

### Related Problems:

```
├─ Find Peak in 2D Array
├─ Find Peak Element II
├─ Find Local Minima
└─ Search in Rotated Array (similar slope idea)
```

---

## 🎯 Edge Cases & Handling

### Edge Case 1: Single Element

```
Array: [1]
Peak: 1

Boundaries: nums[-1]=-∞, nums[1]=-∞
1 > -∞? YES
Peak at index 0 ✓

low=0, high=0
loop immediately ends
return 0 ✓
```

### Edge Case 2: Two Elements (Increasing)

```
Array: [1, 2]
Peak: 2

1 < 2? YES
→ low = 1

low=1, high=1
Return 1 ✓
```

### Edge Case 3: Two Elements (Decreasing)

```
Array: [2, 1]
Peak: 2

low=0, high=1
mid=0, nums[0]=2, nums[1]=1
2 < 1? NO
→ high = 0

low=0, high=0
Return 0 ✓
```

### Edge Case 4: Strictly Increasing

```
Array: [1, 2, 3, 4, 5]
Peak: 5 (at end, with -∞ boundary)

Keep moving right as nums[mid] < nums[mid+1]
Eventually reach index 4
return 4 ✓
```

### Edge Case 5: Strictly Decreasing

```
Array: [5, 4, 3, 2, 1]
Peak: 5 (at start, with -∞ boundary)

First iteration: nums[0]=5, nums[1]=4
5 < 4? NO
→ high = 0

Return 0 ✓
```

### Edge Case 6: Flat Array

```
Array: [5, 5, 5, 5]
Peak: Any index (all are peaks technically)

Algorithm returns first or some valid index ✓
```

---

## 🎤 Interview Signals & Tips

### Interviewer Puchega: "Kyun Slope Logic?"

**Your Answer:**
```
"Array sorted nahi hai, toh binary search
normally kaam nahi karey.

Par ye observation karey:
- Increasing part: Peak aage
- Decreasing part: Peak piche

Slope just indicate karey direction.

Guarantee: Peak zaroori hai kyunki
array ke ends -∞ hain (logical boundary).

Ye guarantee binary search enable karey O(log n) mein!"
```

### Interviewer Puchega: "Why `nums[mid] < nums[mid+1]`?"

**Your Answer:**
```
"Ye check karey: 'Peak right side mein aage?'

Agar nums[mid] < nums[mid+1]:
  → Increasing trend
  → Values up jaa rahe hain
  → Peak aage jah ayega

Agar nums[mid] > nums[mid+1]:
  → Decreasing trend
  → Peak piche hai

Ye simple slope check!"
```

### Interviewer Puchega: "Can Return Any Peak?"

**Your Answer:**
```
"Haan! Problem explicitly kehta hai:
'If multiple peaks, return any'

Algorithm first peak find karey
aur return kar dey.

Jo slope condition match karey,
wo peak mein se koi ek mil jayega!"
```

### Interviewer Puchega: "Time Complexity?"

**Your Answer:**
```
"O(log n)!

Har iteration mein:
├─ Search space half hota hai
├─ Either low = mid + 1
├─ Or high = mid
└─ Exponential reduction

Log₂(n) iterations maximum.

Space: O(1)"
```

---

## 🚨 Common Mistakes (Avoid These!)

### Mistake 1: Comparing Wrong Neighbors

```
❌ WRONG:
if nums[mid] > nums[mid - 1]:
  (Only left check, incomplete!)

✓ CORRECT:
if nums[mid] < nums[mid + 1]:
  (Check right to detect slope direction)
```

### Mistake 2: Using `low <= high`

```
❌ WRONG:
while low <= high:
  (Might cause extra iteration issues)

✓ CORRECT:
while low < high:
  (Clean termination when low == high)
```

### Mistake 3: Incrementing/Decrementing Wrong

```
❌ WRONG:
if nums[mid] < nums[mid + 1]:
  high = mid    // Wrong direction!

✓ CORRECT:
if nums[mid] < nums[mid + 1]:
  low = mid + 1 // Right direction!
```

### Mistake 4: Accessing Out of Bounds

```
❌ WRONG:
if nums[mid] < nums[mid + 1]:
  (What if mid = n-1? mid+1 out of bounds!)

✓ CORRECT:
Use while condition: while low < high
This ensures mid + 1 is always valid!
```

### Mistake 5: Forgetting Boundary Condition

```
❌ WRONG:
"Peak sirf internal elements mein hota"

✓ CORRECT:
"Boundaries = -∞, toh start/end bhi peak ho sakte!"
Algorithm handles automatically.
```

### Mistake 6: Thinking Peak Unique

```
❌ WRONG:
"Array mein sirf ek peak hota"

✓ CORRECT:
"Multiple peaks ho sakte! Any one return karo"
Algorithm finds any valid peak.
```

### Mistake 7: Complex Conditions

```
❌ WRONG:
if (nums[mid] > nums[mid-1] AND 
    nums[mid] > nums[mid+1]):
  (Explicit peak check - misses slope advantage!)

✓ CORRECT:
if nums[mid] < nums[mid + 1]:
  (Slope-based, simpler, faster)
```

---

## 📝 Revision Notes (Quick Summary)

### Algorithm Logic

```
CORE LOGIC:
├─ Compare nums[mid] vs nums[mid+1]
├─ Detect slope direction
│
├─ If nums[mid] < nums[mid+1]:
│  └─ Upslope! Peak right mein
│  └─ low = mid + 1
│
└─ If nums[mid] >= nums[mid+1]:
   └─ Downslope! Peak left or at mid
   └─ high = mid

LOOP: while low < high
RETURN: low (== high when ends)
```

### Key Concepts

```
SLOPE-BASED THINKING:
├─ Increasing = Peak ahead
├─ Decreasing = Peak behind
└─ This guides search!

GUARANTEE:
├─ Boundaries = -∞
├─ Array continues up/down
└─ Peak zaroori hai!

OPTIMIZATION:
├─ Use slope, not explicit check
├─ Binary search O(log n)
└─ Simple elegant solution
```

---

## 🔗 Related Problems

1. **Find Peak in 2D Array** → Similar slope concept, 2D version
2. **Find Peak Element II** → Different twist on peaks
3. **Local Minima** → Opposite of peak
4. **Mountain Peak Finding** → Extended version
5. **Search in Rotated Array** → Similar slope-based idea

---

## 📊 Algorithm Summary Table

```
Aspect              Details
─────────────────────────────────────
Approach            Slope-based binary search
Time Complexity     O(log n) ✓
Space Complexity    O(1) ✓
Key Comparison      nums[mid] vs nums[mid+1]
Direction Logic     Upslope → go right
                    Downslope → go left
Boundary Handling   -∞ on both sides
Multiple Peaks      Return any valid
Best For            Interview optimal solution
```

---

## ✅ Self-Check Checklist

- [ ] Peak definition samjh aata hai?
- [ ] Slope concept clear hai?
- [ ] nums[mid] < nums[mid+1] logic?
- [ ] low = mid + 1 vs high = mid difference?
- [ ] `low < high` condition clear?
- [ ] Boundary condition (-∞) understood?
- [ ] Multiple peaks handling?
- [ ] Edge cases: single, two, strictly inc/dec?
- [ ] O(log n) intuition?
- [ ] Why slope works?

---

## 💡 Final Insight: Slope = Direction Guide

```
CORE PROPERTY:

In any array:
"At any point, slope tells direction to peak"

Why?
├─ If going up: peak ahead (higher side)
├─ If going down: peak behind (lower side)
├─ Array mein peak zaroori hoga
│  (Because boundaries = -∞)
└─ So binary search guaranteed to find!

This mountain-climbing intuition
makes the solution elegant!
```

---

## 🎯 Decision Flow

```
Peak finding problem?
  ├─ Array sorted?
  │  └─ Might be rotated (different approach)
  │
  ├─ Array unsorted, any peak ok?
  │  └─ This algorithm perfect ✓
  │
  ├─ O(log n) required?
  │  └─ Slope-based binary search ✓
  │
  └─ Multiple peaks possible?
     └─ Algorithm handles (returns any) ✓
```

---

**Happy Learning! Find Peak Element clear ho gaye! 🚀**