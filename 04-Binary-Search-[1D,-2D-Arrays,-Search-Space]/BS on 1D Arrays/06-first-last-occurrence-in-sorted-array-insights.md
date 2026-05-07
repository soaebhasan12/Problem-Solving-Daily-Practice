# First aur Last Occurrence in Sorted Array
## Complete Learning Guide (Hinglish) 🎯

---

## 📚 Problem Statement (Hindi mein)

**Sorted array diya, target element ke:**
- **First Position:** Pehla index jahan target hai
- **Last Position:** Aakhri index jahan target hai

Agar target nahi mila → `[-1, -1]` return karo

### Example samjho:
```
Array: [5, 7, 7, 8, 8, 10]
Target: 8

First Occurrence: Index 3 (pehla 8)
Last Occurrence: Index 4 (aakhri 8)
Output: [3, 4]

---

Array: [5, 7, 7, 8, 8, 10]
Target: 6

First Occurrence: -1 (6 nahi hai)
Last Occurrence: -1
Output: [-1, -1]

---

Array: [5, 7, 7, 8, 8, 10]
Target: 7

First Occurrence: Index 1 (pehla 7)
Last Occurrence: Index 2 (aakhri 7)
Output: [1, 2]
```

---

## 🧠 Core Intuition: Duplicates ke Boundaries

### Problem Ka Real Challenge

```
Exact Match Binary Search:
  Target dhund, mil gaya? → Return!
  
YEH PROBLEM:
  Target mil gaya, par aur bhi ho sakte hain!
  ├─ Leftmost (pehla) dhundo
  ├─ Rightmost (aakhri) dhundo
  └─ Dono boundaries chahiye!

Intuition:
"Element mil gaya, par sirf isko nahi...
 Uske aas-paas aur kaunse hain?"
```

### Visual Understanding

```
Array: [5, 7, 7, 7, 8, 8, 10]
Index:  0  1  2  3  4  5   6

Target: 7

Normal Binary Search:
  Mid = 3, nums[3] = 7
  Found! Return 3
  (Par yeh middle 7 hai, first/last nahi!)

Ye Problem:
  First 7: Index 1 ← Pehla
  Last 7:  Index 3 ← Aakhri
  Output: [1, 3]
```

---

## 🎯 Concept 1: First Occurrence (Leftmost)

### Definition
**First Occurrence** = Sorted array mein **pehla index jahan target == element**

```
Hindi: "Target element ka pehla position"
```

### Intuition Samjho

```
Array: [5, 7, 7, 7, 8, 8, 10]
Target: 7

Sochte hain:
- Index 0: 5 == 7? Nahi
- Index 1: 7 == 7? HAN! (First occurrence)
- Index 2: 7 == 7? HAN! Par pehla toh 1 hai
- Index 3: 7 == 7? HAN! Par pehla toh 1 hai

Answer: 1 (pehla index)
```

### Direction Logic: Kyun LEFT Mein Jaate Ho?

```
FIRST OCCURRENCE CONDITION: if nums[mid] == target

Scenario 1: nums[mid] == target
  first = mid              (Found! Store kro)
  high = mid - 1           (Kyun LEFT? Aur pehle aage ho sakta hai!)
  
  Example: [7, 7, 7]
  Found middle 7 at index 1
  Par left mein bhi 7 hai (index 0)
  Check kar left!

Scenario 2: nums[mid] < target
  low = mid + 1            (RIGHT mein dekho)

Scenario 3: nums[mid] > target
  high = mid - 1           (LEFT mein dekho)
```

### Visual: Direction Samjho

```
Array: [5, 7, 7, 7, 8, 8, 10]
Index:  0  1  2  3  4  5   6

Target: 7
Find: FIRST (leftmost)

Mid = 3, nums[3] = 7
       ↓
      FOUND!
      ↓
Par pehla 7 kahan hai?
LEFT side mein! (Index 1)
↓
high = mid - 1 (LEFT jao)

Continue search LEFT...
Mil jayega!
```

---

## 🎯 Concept 2: Last Occurrence (Rightmost)

### Definition
**Last Occurrence** = Sorted array mein **aakhri index jahan target == element**

```
Hindi: "Target element ka aakhri position"
```

### Intuition Samjho

```
Array: [5, 7, 7, 7, 8, 8, 10]
Target: 7

Sochte hain:
- Index 1: 7 == 7? HAN! Par aakhri toh?
- Index 2: 7 == 7? HAN! Par aakhri toh?
- Index 3: 7 == 7? HAN! (Last occurrence!)
- Index 4: 8 == 7? Nahi

Answer: 3 (aakhri index)
```

### Direction Logic: Kyun RIGHT Mein Jaate Ho?

```
LAST OCCURRENCE CONDITION: if nums[mid] == target

Scenario 1: nums[mid] == target
  last = mid               (Found! Store kro)
  low = mid + 1            (Kyun RIGHT? Aur aage aage ho sakta hai!)
  
  Example: [7, 7, 7]
  Found middle 7 at index 1
  Par right mein bhi 7 hai (index 2)
  Check kar right!

Scenario 2: nums[mid] < target
  low = mid + 1            (RIGHT mein dekho)

Scenario 3: nums[mid] > target
  high = mid - 1           (LEFT mein dekho)
```

### Visual: Direction Samjho

```
Array: [5, 7, 7, 7, 8, 8, 10]
Index:  0  1  2  3  4  5   6

Target: 7
Find: LAST (rightmost)

Mid = 3, nums[3] = 7
       ↓
      FOUND!
      ↓
Par aakhri 7 kahan hai?
RIGHT side mein! (Index 3 itself, ya aage?)
↓
low = mid + 1 (RIGHT jao)

Continue search RIGHT...
Mil jayega!
```

---

## 🔄 First vs Last: Side-by-Side

```
                FIRST                   LAST
              ────────                ────────
Goal:         Leftmost ==             Rightmost ==
Condition:    == target               == target

Found?
  first = mid                          last = mid
  high = mid - 1                       low = mid + 1
  Move LEFT!                           Move RIGHT!

Invalid:
  mid < target → low = mid + 1
  mid > target → high = mid - 1

Why?
  First: Aur pehle element             Last: Aur aage element
         LEFT side mein                       RIGHT side mein
         (Left search)                        (Right search)

Pattern:
  == (and want LEFT) → high = mid - 1
  == (and want RIGHT) → low = mid + 1
```

---

## 📝 Pseudo Code (Step-by-Step)

### First Occurrence Pseudo Code

```
FIRST_OCCURRENCE(nums, target):
  
  low = 0
  high = n - 1
  first = -1                  // Default: nahi mila
  
  WHILE low <= high:
    mid = (low + high) / 2
    
    IF nums[mid] == target:
      first = mid             // Store kro (potential first)
      high = mid - 1          // LEFT mein dekho (pehla chahiye)
    ELSE IF nums[mid] < target:
      low = mid + 1           // RIGHT mein dekho
    ELSE:
      high = mid - 1          // LEFT mein dekho
  
  RETURN first


INTUITION:
├─ == mil gaya? Store + LEFT search
├─ Why LEFT? Aur pehle element ho sakta hai
└─ Loop ends → first tera answer (leftmost index)
```

### Last Occurrence Pseudo Code

```
LAST_OCCURRENCE(nums, target):
  
  low = 0
  high = n - 1
  last = -1                   // Default: nahi mila
  
  WHILE low <= high:
    mid = (low + high) / 2
    
    IF nums[mid] == target:
      last = mid              // Store kro (potential last)
      low = mid + 1           // RIGHT mein dekho (aakhri chahiye)
    ELSE IF nums[mid] < target:
      low = mid + 1           // RIGHT mein dekho
    ELSE:
      high = mid - 1          // LEFT mein dekho
  
  RETURN last


INTUITION:
├─ == mil gaya? Store + RIGHT search
├─ Why RIGHT? Aur aage element ho sakta hai
└─ Loop ends → last tera answer (rightmost index)
```

### Combined (Dono Ek Saath)

```
SEARCH_RANGE(nums, target):
  
  // Step 1: First occurrence dhundo
  first = FIRST_OCCURRENCE(nums, target)
  
  // Step 2: Agar first element hi nahi mila
  IF first == -1:
    RETURN [-1, -1]           // Target nahi hai
  
  // Step 3: Last occurrence dhundo
  last = LAST_OCCURRENCE(nums, target)
  
  RETURN [first, last]
```

---

## 🎬 Dry Run Strategy (Detailed)

### Dry Run Kaise Karey?

#### Key: Both Variables Track Karo!

```
IMPORTANT:
"First + Last dono track karo!

Iteration ke baad dekho:
- Kya first/last update hua?
- Kyun low/high badla?
- Target se match? < ? >?

Clear picture milti hai!"
```

---

## 📊 Dry Run Example 1: First Occurrence

```
Array: [5, 7, 7, 8, 8, 10]
Target: 7

FIRST OCCURRENCE SEARCH:

Initial State:
  low=0, high=5, first=-1
  Find: == 7 (leftmost)

|---|---|---|---|---|---|
| 5 | 7 | 7 | 8 | 8 |10 |
  0   1   2   3   4   5

Iteration 1:
  low=0, high=5
  mid = (0+5)/2 = 2
  nums[2] = 7
  
  7 == 7? YES! ✓
  └─ first = 2 (store!)
  └─ high = 2 - 1 = 1
  
  Status: Found at 2, par pehla ho sakta?
          LEFT dekho!

|---|---|---|---|---|---|
| 5 | 7 | 7 | 8 | 8 |10 |
  0  [1] 2   3   4   5
      ↑
    High move here

Iteration 2:
  low=0, high=1
  mid = (0+1)/2 = 0
  nums[0] = 5
  
  5 == 7? NO
  5 < 7? YES
  └─ low = 0 + 1 = 1
  
  Status: 5 chhota, RIGHT dekho
          first = 2 (unchanged)

Iteration 3:
  low=1, high=1
  mid = (1+1)/2 = 1
  nums[1] = 7
  
  7 == 7? YES! ✓
  └─ first = 1 (better! aur pehla)
  └─ high = 1 - 1 = 0
  
  Status: Found at 1, LEFT dekho bhi (pehla ho?)

Iteration 4:
  low=1, high=0
  low > high → LOOP ENDS
  
RETURN first = 1 ✓

Trace:
  first: -1 → 2 → 1
  Leftmost 7 = Index 1 ✓
```

---

## 📊 Dry Run Example 2: Last Occurrence

```
Array: [5, 7, 7, 8, 8, 10]
Target: 8

LAST OCCURRENCE SEARCH:

Initial State:
  low=0, high=5, last=-1
  Find: == 8 (rightmost)

|---|---|---|---|---|---|
| 5 | 7 | 7 | 8 | 8 |10 |
  0   1   2   3   4   5

Iteration 1:
  low=0, high=5
  mid = (0+5)/2 = 2
  nums[2] = 7
  
  7 == 8? NO
  7 < 8? YES
  └─ low = 2 + 1 = 3
  
  Status: 7 chhota, RIGHT dekho
          last = -1 (unchanged)

|---|---|---|---|---|---|
| 5 | 7 | 7 | 8 | 8 |10 |
  0   1   2  [3] 4   5
              ↑
            Low move here

Iteration 2:
  low=3, high=5
  mid = (3+5)/2 = 4
  nums[4] = 8
  
  8 == 8? YES! ✓
  └─ last = 4 (store!)
  └─ low = 4 + 1 = 5
  
  Status: Found at 4, RIGHT dekho (aage ho sakta?)

|---|---|---|---|---|---|
| 5 | 7 | 7 | 8 | 8 |10 |
  0   1   2   3  [4] 5
                  ↑
                Low move here

Iteration 3:
  low=5, high=5
  mid = (5+5)/2 = 5
  nums[5] = 10
  
  10 == 8? NO
  10 < 8? NO
  10 > 8? YES
  └─ high = 5 - 1 = 4
  
  Status: 10 bada, LEFT dekho
          last = 4 (unchanged)

Iteration 4:
  low=5, high=4
  low > high → LOOP ENDS
  
RETURN last = 4 ✓

Trace:
  last: -1 → 4
  Rightmost 8 = Index 4 ✓
```

---

## 📊 Dry Run Example 3: Search Range (Combined)

```
Array: [5, 7, 7, 8, 8, 10]
Target: 7

COMBINED SEARCH:

Step 1: First Occurrence
  (See dry run 1)
  Result: first = 1

Step 2: Check if Found
  first == -1? NO (1 != -1)
  → Continue to step 3

Step 3: Last Occurrence
  low=0, high=5, last=-1
  
  Iteration 1:
    mid=2, nums[2]=7
    7==7? YES
    last=2, low=3
  
  Iteration 2:
    mid=4, nums[4]=8
    8==7? NO, 8>7
    high=3
  
  Iteration 3:
    mid=3, nums[3]=8
    8==7? NO, 8>7
    high=2
  
  Iteration 4:
    low=3, high=2
    low > high → LOOP ENDS
  
  Result: last = 2

FINAL OUTPUT: [1, 2] ✓
```

---

## 🎓 3 Approaches: Comparison

### Approach 1: Direct First + Last Binary Search

```
PROS:
├─ O(log n) time complexity ✓
├─ Space efficient ✓
├─ Dono searches separate (clean logic) ✓
└─ Duplicates handle perfectly ✓

CONS:
├─ Do binary searches run karne padey
└─ Code thoda lengthy (dono functions)

BEST FOR: Interview prep, optimal solution
```

### Approach 2: Lower Bound + Upper Bound

```
Algorithm:
├─ Lower Bound: First >= target
├─ Upper Bound: First > target - 1
├─ Check: nums[lb] == target?
└─ Return: [lb, ub-1] or [-1, -1]

PROS:
├─ Ek pattern (Lower/Upper Bound) reuse
├─ Code DRY (Don't Repeat Yourself)
└─ Clean boundaries concept

CONS:
├─ Thoda abstract (conceptually harder)
├─ O(log n) + O(log n) = O(log n) anyway
└─ Interview mein pehle approach better

BEST FOR: Pattern recognition, advanced candidates
```

### Approach 3: Linear Traverse (Brute Force)

```
Algorithm:
├─ Start index 0, end index n-1
├─ Loop: i = 0 to n-1
├─ first target mila → first = i
├─ har bar last = i update kro
└─ Return [first, last]

PROS:
├─ Simple samjh mein aata
├─ Straight-forward logic
└─ No edge case confusion

CONS:
├─ O(n) time complexity ❌
├─ Sorted array ka fayda nahi
└─ Interview mein reject hoga
   (problem mein O(log n) required!)

BEST FOR: Initial understanding only
```

### Comparison Table

```
Approach          Time    Space   Optimal?   Best For
──────────────────────────────────────────────────────
1. First+Last BS  O(logn) O(1)    YES ✓      Interviews
2. LB+UB BS       O(logn) O(1)    YES ✓      Advanced
3. Linear         O(n)    O(1)    NO ❌      Learning
```

---

## 🎯 Pattern Recognition

### Yeh Problem Family Recognize Karo

```
Binary Search on EXACT MATCH + DUPLICATES:

├─ First Occurrence (Leftmost ==)
├─ Last Occurrence (Rightmost ==)
├─ Search Range (First + Last)
└─ Find K Closest Elements
    (involving First/Last position)
```

### When Pattern Activate?

```
Signal 1: Sorted array
Signal 2: Duplicates possible
Signal 3: Position/range chahiye (not just presence)
Signal 4: O(log n) requirement

→ First + Last binary search pattern!
```

### Direction Logic Pattern

```
RULE: == condition + direction

Want Leftmost?
  == mil gaya → LEFT jao (high = mid - 1)
  
Want Rightmost?
  == mil gaya → RIGHT jao (low = mid + 1)

Other comparisons (<, >):
  Normal binary search (left/right based on value)
```

---

## 🎬 Edge Cases & Handling

### Edge Case 1: Target Nahi Hai

```
Array: [1, 3, 5, 7]
Target: 6

First Occurrence:
  mid=2, nums[2]=5
  5==6? NO, 5<6 → low=3
  
  mid=3, nums[3]=7
  7==6? NO, 7>6 → high=2
  
  low > high → first=-1

Last Occurrence:
  Same logic → last=-1

Output: [-1, -1] ✓
```

### Edge Case 2: Array Mein Ek Hi Element

```
Array: [5]
Target: 5

First: mil gaya at index 0
Last: mil gaya at index 0
Output: [0, 0] ✓

---

Array: [5]
Target: 3

First: nahi mila (-1)
Last: nahi mila (-1)
Output: [-1, -1] ✓
```

### Edge Case 3: Target First Element

```
Array: [5, 7, 8, 10]
Target: 5

First:
  mid=2, 8>5 → high=1
  mid=0, 5==5 → first=0, high=-1
  Loop ends → first=0 ✓

Last:
  mid=2, 8>5 → high=1
  mid=0, 5==5 → last=0, low=1
  low > high → last=0 ✓

Output: [0, 0] ✓
```

### Edge Case 4: Target Last Element

```
Array: [5, 7, 8, 10]
Target: 10

First:
  mid=2, 8<10 → low=3
  mid=3, 10==10 → first=3, high=2
  Loop ends → first=3 ✓

Last:
  mid=2, 8<10 → low=3
  mid=3, 10==10 → last=3, low=4
  low > high → last=3 ✓

Output: [3, 3] ✓
```

### Edge Case 5: All Duplicates

```
Array: [5, 5, 5, 5, 5]
Target: 5

First:
  Iterate: 2 → 1 → 0 (leftmost)
  first=0 ✓

Last:
  Iterate: 2 → 3 → 4 (rightmost)
  last=4 ✓

Output: [0, 4] ✓
```

### Edge Case 6: Empty Array

```
Array: []
Target: 5

First: low > high immediately → first=-1
Last: low > high immediately → last=-1

Output: [-1, -1] ✓
```

---

## 🎤 Interview Signals & Tips

### Interviewer Puchega: "Kyun Dono Separate Searches?"

**Your Answer:**
```
"Kyunki dono ki direction opposite hain:

First Occurrence:
  Element mil gaya → HIGH = MID - 1 (LEFT)
  Kyunki pehla chahiye (aur pehle element ho sakte)

Last Occurrence:
  Element mil gaya → LOW = MID + 1 (RIGHT)
  Kyunki aakhri chahiye (aur aage element ho sakte)

Ek hi search mein dono conditions combine nahi kar sakte!
Alag alag binary searches necessary hain."
```

### Interviewer Puchega: "Why Check `first == -1`?"

**Your Answer:**
```
"Optimization ke liye!

Agar first == -1, matlab target hi array mein nahi hai.
Toh last search karne ki kya zaroorat?

├─ Direct return [-1, -1]
├─ Ek binary search save ho gaya
└─ Time save, logic clear"
```

### Interviewer Puchega: "Can We Use Lower/Upper Bound?"

**Your Answer:**
```
"Haan! Lower + Upper Bound bhi work karey:

Lower Bound: First >= target
Upper Bound: First > target

Agar nums[lb] == target:
  └─ [lb, ub-1] = [first, last]
Else:
  └─ [-1, -1]

BUT, direct approach zyada simple aur intuitive hai.
Both O(log n) anyway!"
```

### Interviewer Puchega: "Time Complexity?"

**Your Answer:**
```
"O(log n)!

First search: O(log n)
Last search: O(log n)
Total: O(log n) + O(log n) = O(log n)
(constants matter nahi asymptotically)

Space: O(1) (sirf variables)"
```

---

## 🚨 Common Mistakes (Avoid These!)

### Mistake 1: Mixing Directions

```
❌ WRONG:
FIRST (want LEFT):
  if nums[mid] == target:
    first = mid
    low = mid + 1        // RIGHT gaya! Wrong!

✓ CORRECT:
FIRST (want LEFT):
  if nums[mid] == target:
    first = mid
    high = mid - 1       // LEFT jao
```

### Mistake 2: Forget to Check `first == -1`

```
❌ WRONG:
first = FIRST_OCCURRENCE(nums, target)
last = LAST_OCCURRENCE(nums, target)  // Unnecessary!
return [first, last]

(Agar target nahi, last search free!)

✓ CORRECT:
first = FIRST_OCCURRENCE(nums, target)
if first == -1:
  return [-1, -1]       // Early return
last = LAST_OCCURRENCE(nums, target)
return [first, last]
```

### Mistake 3: Using Wrong Comparisons

```
❌ WRONG:
FIRST:
  if nums[mid] < target:    // For finding first!
    ...                      (This is brute force logic)

✓ CORRECT:
FIRST:
  if nums[mid] == target:   // == condition!
    first = mid
    high = mid - 1
  elif nums[mid] < target:
    low = mid + 1
  else:
    high = mid - 1
```

### Mistake 4: Immediate Return After Finding

```
❌ WRONG:
if nums[mid] == target:
  return mid              // Immediately return!

(Ye middle occurrence hai, 
 pehla/aakhri nahi!)

✓ CORRECT:
if nums[mid] == target:
  first = mid             // Store kro
  high = mid - 1          // LEFT jao (pehla dhundo)
```

### Mistake 5: Forgetting Both Variables in Dry Run

```
❌ WRONG DRY RUN:
mid=2, nums[2]==7, high=1
mid=0, nums[0]==5, low=1
...

(Confusing! Kyun low/high badal rahe?)

✓ CORRECT DRY RUN:
Iteration 1:
  mid=2, nums[2]==7? YES
  first=2, high=1 (LEFT jao, pehla dhundo)

Iteration 2:
  mid=0, nums[0]==5? NO
  5<7? YES, low=1

(Clear! Both first aur logic track ho rahe!)
```

### Mistake 6: Different Loop Conditions

```
❌ WRONG:
FIRST search:
  while low < high:       // Different!

LAST search:
  while low <= high:      // Different!

(Edge cases miss ho sakte!)

✓ CORRECT:
BOTH:
  while low <= high:      // Same! Consistent!
```

### Mistake 7: Not Handling Empty Array

```
❌ WRONG:
if nums is empty:
  continue (no check)
  high = nums.length - 1  // Out of bounds!

✓ CORRECT:
if len(nums) == 0:
  return [-1, -1]

OR better:
  Loop condition: while low <= high
  Automatically handles empty
```

### Mistake 8: Confusing with Exact Match Binary Search

```
❌ WRONG (Exact Match Logic):
if nums[mid] == target:
  return mid              // Wrong for this problem!

✓ CORRECT (First/Last Logic):
if nums[mid] == target:
  ans = mid               // Store (potential answer)
  direction = LEFT/RIGHT  // Continue search!
```

---

## 📝 Revision Notes (Quick Summary)

### First Occurrence (Leftmost ==)

```
FIRST OCCURRENCE:
├─ Goal: Pehla index jahan target == element
├─ Condition: if nums[mid] == target
├─ Direction: high = mid - 1 (LEFT)
├─ Why LEFT: Aur pehle element dhundo
├─ Default: first = -1
└─ Answer: Aakhri stored value (leftmost)

Pattern:
  == found? Store + LEFT search
  Continue until loop ends
```

### Last Occurrence (Rightmost ==)

```
LAST OCCURRENCE:
├─ Goal: Aakhri index jahan target == element
├─ Condition: if nums[mid] == target
├─ Direction: low = mid + 1 (RIGHT)
├─ Why RIGHT: Aur aage element dhundo
├─ Default: last = -1
└─ Answer: Aakhri stored value (rightmost)

Pattern:
  == found? Store + RIGHT search
  Continue until loop ends
```

### Search Range (Combined)

```
SEARCH RANGE:
├─ Step 1: First = FIRST_OCCURRENCE()
├─ Step 2: if first == -1 → return [-1, -1]
├─ Step 3: Last = LAST_OCCURRENCE()
└─ Step 4: return [first, last]

Key: Optimization (early return)
```

### Direction Logic Summary

```
== CONDITION + DIRECTION LOGIC:

Want FIRST (Leftmost)?
  == mil gaya → Store + HIGH = MID - 1

Want LAST (Rightmost)?
  == mil gaya → Store + LOW = MID + 1

Why opposite?
  First: Chhotey end mein dekho (LEFT)
  Last: Bade end mein dekho (RIGHT)
```

---

## 🔗 Related Problems

1. **Find the Duplicate Number** → Boundary + duplicates
2. **Search in Rotated Sorted Array II** → Duplicates ka challenge
3. **Find K Closest Elements** → First/Last position use
4. **Smallest Missing Positive** → Similar boundary logic
5. **H-Index II** → Modified binary search with position

---

## 📊 Approaches Comparison Table

```
Approach          Time      Space   Difficulty   Use
──────────────────────────────────────────────────────
Direct BS         O(log n)  O(1)    Medium       BEST
LB+UB BS          O(log n)  O(1)    Hard         Advanced
Linear Traverse   O(n)      O(1)    Easy         Learning
```

---

## ✅ Self-Check Checklist

- [ ] First Occurrence = Leftmost ==? (LEFT search)
- [ ] Last Occurrence = Rightmost ==? (RIGHT search)
- [ ] Directions opposite?
- [ ] Early return check: `first == -1`?
- [ ] == condition track karey dry run?
- [ ] Comparisons: ==, <, > sab clear?
- [ ] Edge cases: empty, single, all duplicates?
- [ ] Time complexity O(log n)?
- [ ] Space complexity O(1)?
- [ ] Brute force vs optimal?

---

## 🎯 Decision Matrix: Which Approach?

```
Interview Setting?
  ├─ Pehli bar → Direct First+Last approach ✓
  ├─ Advanced Questions → Lower+Upper Bound
  └─ Time Limited → Straight approach

Why?
  ├─ Direct: Simple, intuitive, less bugs
  ├─ LB+UB: Pattern recognition, elegant
  └─ Linear: No (violates O(log n) requirement)
```

---

## 💡 Key Insight: Store + Continue Pattern

```
CORE DIFFERENCE:

Exact Match Binary Search:
  if found:
    return immediately
    
First/Last Binary Search:
  if found:
    store answer
    continue searching
    (better/other occurrence mil sakta!)
  
YEH PATTERN is applicable to:
├─ Floor & Ceil
├─ First & Last Occurrence
├─ Lower & Upper Bound
└─ Other boundary problems
```

---

**Happy Learning! First + Last Occurrence clear ho gaye! 🚀**
