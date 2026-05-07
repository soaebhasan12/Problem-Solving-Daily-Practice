# Floor aur Ceil in Sorted Array
## Complete Learning Guide (Hinglish) 🎯

---

## 📚 Problem Statement (Hindi mein)

**Sorted array diya ek target number ke saath. Dhundo:**
- **Floor (x):** Array mein largest element jo `x` se **chhota ya barabar** ho
- **Ceil (x):** Array mein smallest element jo `x` se **bada ya barabar** ho

Agar nahi mila → `-1` return karo

### Example samjho:
```
Array: [3, 4, 4, 7, 8, 10]
Target: 5

Floor(5) = 4  (5 se chhota largest = 4)
Ceil(5) = 7   (5 se bada smallest = 7)

---

Array: [3, 4, 4, 7, 8, 10]
Target: 8

Floor(8) = 8  (8 se chhota ya barabar largest = 8 itself)
Ceil(8) = 8   (8 se bada ya barabar smallest = 8 itself)

---

Array: [3, 4, 4, 7, 8, 10]
Target: 2

Floor(2) = -1  (2 se chhota kuch nahi)
Ceil(2) = 3    (2 se bada ya barabar = 3)
```

---

## 🧠 Core Intuition: Boundary Binary Search

### Isse Pehle Samjho: Exact vs Boundary Search

#### **Exact Match Search (Normal Binary Search)**
```
Target = 5
Array: [1, 3, 5, 7, 9]

Goal: 5 dhundo (exact match)
       ↓
      Index 2

Answer: Either mil gaya ya nahi!
Stop! ✓
```

#### **Boundary Search (Ye problem!)**
```
Target = 5
Array: [1, 3, 4, 7, 9]

Goal: 5 nahi hai
Par dhundo: Kaunsa element 5 ke closest hain?
           - Chhota side: 4 (Floor)
           - Bada side: 7 (Ceil)

Answer: Continue search karna padega!
Par "valid answer" store karte chalenge...
```

---

## 💡 Key Insight: Answer Store + Search Continue

### Ye Concept Samjho! (Most Important)

```
Normal Binary Search:
  Match Mila? → Return immediately
  ❌ Match Nahi? → Return -1

Boundary Search (Floor/Ceil):
  Valid Condition Mila? → Store answer BUT continue search!
  ❌ Never Found? → Return stored answer
  
  Because: Aur bhi better (closer) answer ho sakta hai!
```

### Visual Example:

```
Array: [3, 4, 4, 7, 8, 10]
Target: 5

Normal Binary Search:
  5 dhund: Nahi mila → Return -1

Floor Search:
  Step 1: 7 dekha → 7 > 5 → Search left
  Step 2: 4 dekha → 4 <= 5 → Store 4 as answer BUT continue left
  Step 3: 3 dekha → 3 <= 5 → Store 3? Nahi! (aur chhota ho gaya)
  Step 4: Loop ends
  Return: 4 (sabse baad stored valid answer)
```

---

## 🎯 Concept 1: CEIL (Ceiling)

### Definition
**Ceil(x)** = Smallest element ≥ x

```
English: "Smallest element greater than or equal to x"
Hindi: "x se bada ya barabar sabse chhota element"
```

### Intuition Samjho

```
Array: [3, 4, 4, 7, 8, 10]
Target: 5

Sochte hain:
- 3 ≥ 5? Nahi
- 4 ≥ 5? Nahi
- 7 ≥ 5? HAN! → Valid answer
- 8 ≥ 5? HAN! → Valid par bada than 7
- 10 ≥ 5? HAN! → Valid par bada than 8

Toh smallest ≥ 5 = 7 ✓
```

### Direction Logic: Kyun LEFT Mein Jaate Ho?

```
CEIL CONDITION: if nums[mid] >= target

Scenario 1: nums[mid] >= target
  ans = nums[mid]        (Valid answer mil gaya! Store kro)
  high = mid - 1         (Par aur bhi CHHOTA ≥ element ho sakta hai!)
  
  Kyun?
  Valid toh hai, par chhota element chahiye
  Toh LEFT mein dekho!

Scenario 2: nums[mid] < target
  low = mid + 1          (RIGHT mein dekho, bada element chahiye)
```

### Visual: Direction Samjho

```
Target: 5
Array: [1, 2, 3, 4, 7, 8, 9, 10]
                      ↑
                    Found 7 (≥ 5)
                    
                    Kya 4 ≥ 5? Nahi
                    So LEFT mein bhi answer nahi hoga!
                    
                    ✓ CORRECT: Aap 7 ke LEFT dekh rahe ho
                                (aur chhota valid answer paoge)

Analogy:
"Aapko smallest change chahiye 5 rupees se."
₹10 mila (valid)
Par ₹7 bhi hoga LEFT side mein?
Check kar lo!
```

---

## 🎯 Concept 2: FLOOR (Floor)

### Definition
**Floor(x)** = Largest element ≤ x

```
English: "Largest element less than or equal to x"
Hindi: "x se chhota ya barabar sabse bada element"
```

### Intuition Samjho

```
Array: [3, 4, 4, 7, 8, 10]
Target: 5

Sochte hain:
- 3 ≤ 5? HAN! → Valid answer
- 4 ≤ 5? HAN! → Valid par chhota than 5
- 7 ≤ 5? Nahi
- 8 ≤ 5? Nahi
- 10 ≤ 5? Nahi

Toh largest ≤ 5 = 4 ✓
```

### Direction Logic: Kyun RIGHT Mein Jaate Ho?

```
FLOOR CONDITION: if nums[mid] <= target

Scenario 1: nums[mid] <= target
  ans = nums[mid]        (Valid answer mil gaya! Store kro)
  low = mid + 1          (Par aur bhi BADA ≤ element ho sakta hai!)
  
  Kyun?
  Valid toh hai, par bada element chahiye
  Toh RIGHT mein dekho!

Scenario 2: nums[mid] > target
  high = mid - 1         (LEFT mein dekho, chhota element chahiye)
```

### Visual: Direction Samjho

```
Target: 5
Array: [1, 2, 3, 4, 7, 8, 9, 10]
            ↑
          Found 4 (≤ 5)
          
          Kya 7 ≤ 5? Nahi
          So RIGHT mein answer nahi hoga... 
          
          Par WAIT! 4 ke RIGHT mein 4 hi hai (duplicate)
          Shayad aur bhi 4 ho ya... nahi, 7 aa gaya
          
          ✓ CORRECT: Aap 4 ke RIGHT dekh rahe ho
                      (aur bada valid answer dhundne ke liye)

Analogy:
"Aapko largest coin chahiye jo 5 rupees se kam ho."
₹4 mila (valid)
Par ₹3 bhi hoga RIGHT side mein?
Nahi, par ₹4 duplicate ho sakta hai!
Check kar lo!
```

---

## 🔄 Why Continue Searching After Valid Answer?

### Ye Samjho! (Critical Concept)

#### Ceil ke saath:
```
Valid Condition: >= mila

Example:
Array: [1, 2, 5, 5, 5, 8, 10]
Target: 5

Mid = 2, nums[2] = 5 (≥ 5? YES)
  ans = 5, high = mid - 1
  
Kyun HIGH update karey?
→ Kya 1, 2 mein 5 ≥ 5 wala kuch hai?
→ Nahi! But search continue karna hai
→ Aur CHHOTA answer paoge kya?
→ Search space reduce hota hai, par iska matlab
   nahi ki aur chhota valid answer hoga!

Actually CEIL ke liye:
"Pehla >= element jo milega, wo hi answer!"
But aap LEFT bhi check karoge... kyun?
→ Kyunki BINARY SEARCH algorithm
   aapko "leftmost" >= element chahiye!
```

#### Floor ke saath:
```
Valid Condition: <= mila

Example:
Array: [1, 2, 5, 5, 5, 8, 10]
Target: 5

Mid = 2, nums[2] = 5 (≤ 5? YES)
  ans = 5, low = mid + 1
  
Kyun LOW update karey?
→ RIGHT mein dekho aur BADA ≤ element paoge!
→ 5, 5, 5 mil sakta hai (duplicates)
→ Largest ≤ 5 dhundna hai!

FLOOR ke liye:
"Rightmost <= element dhundo!"
→ Duplicates ko handle karey
→ Sabse bada valid element paoge
```

---

## 📝 Pseudo Code (Step-by-Step)

### CEIL Pseudo Code

```
CEIL(nums, x):
  
  low = 0
  high = n - 1
  ans = -1                    // Default: nahi mila
  
  WHILE low <= high:
    mid = (low + high) / 2
    
    IF nums[mid] >= x:
      ans = nums[mid]         // ✓ Valid! Store kro
      high = mid - 1          // LEFT mein dekho (chhota chahiye)
    ELSE:
      low = mid + 1           // RIGHT mein dekho (bada chahiye)
  
  RETURN ans


INTUITION:
├─ >= condition? → Potential answer
├─ Store kro, par LEFT bhi dekho
└─ Aur chhota valid answer paoge kya?
   → Aage jaoge toh pata chalega!
```

### FLOOR Pseudo Code

```
FLOOR(nums, x):
  
  low = 0
  high = n - 1
  ans = -1                    // Default: nahi mila
  
  WHILE low <= high:
    mid = (low + high) / 2
    
    IF nums[mid] <= x:
      ans = nums[mid]         // ✓ Valid! Store kro
      low = mid + 1           // RIGHT mein dekho (bada chahiye)
    ELSE:
      high = mid - 1          // LEFT mein dekho (chhota chahiye)
  
  RETURN ans


INTUITION:
├─ <= condition? → Potential answer
├─ Store kro, par RIGHT bhi dekho
└─ Aur bada valid answer paoge kya?
   → Aage jaoge toh pata chalega!
```

### COMBINED (Dono ek saath)

```
GET_FLOOR_AND_CEIL(nums, x):
  
  // STEP 1: CEIL DHuNDO
  low = 0, high = n-1, ceil = -1
  WHILE low <= high:
    mid = (low + high) / 2
    IF nums[mid] >= x:
      ceil = nums[mid]
      high = mid - 1
    ELSE:
      low = mid + 1
  
  // STEP 2: FLOOR DHuNDO (alag se!)
  low = 0, high = n-1, floor = -1
  WHILE low <= high:
    mid = (low + high) / 2
    IF nums[mid] <= x:
      floor = nums[mid]
      low = mid + 1
    ELSE:
      high = mid - 1
  
  RETURN (floor, ceil)


IMPORTANT: Alag alag search! Reset karna padta hai!
```

---

## 🎬 Dry Run Strategy (Detailed)

### Dry Run Kaise Karey?

#### Key: Answer Variable Track Karo!

```
IMPORTANT INSIGHT:
"Dry run mein `ans` variable track na karo toh
 loop confusing lagta hai.
 Kyun LOW/HIGH badal rahe ho? Answer mila?
 
 ANS variable dikh jaye, toh samajh aata hai:
 'Haan, answer store hai, par isko improve karey seekhe ho!'"
```

---

## 📊 Dry Run Example 1: Ceil

```
Array: [3, 4, 4, 7, 8, 10]
Target: 5

CEIL SEARCH:

Initial State:
  low=0, high=5, ans=-1
  Target: >= 5 dhundo

|---|---|---|---|---|---|
| 3 | 4 | 4 | 7 | 8 |10 |
  0   1   2   3   4   5

Iteration 1:
  low=0, high=5
  mid = (0+5)/2 = 2
  nums[2] = 4
  
  4 >= 5? NO
  └─ low = 2 + 1 = 3
  
  ans = -1 (still)
  
  Status: 4 chhota hai, RIGHT dekho

|---|---|---|---|---|---|
| 3 | 4 | 4 | 7 | 8 |10 |
  0   1   2  [3] 4   5
              ↑
            Move here

Iteration 2:
  low=3, high=5
  mid = (3+5)/2 = 4
  nums[4] = 8
  
  8 >= 5? YES! ✓
  └─ ans = 8 (store kro!)
  └─ high = 4 - 1 = 3
  
  Status: Answer mil gaya (8), par LEFT dekho
          Kya chhota >= 5 hoga?

|---|---|---|---|---|---|
| 3 | 4 | 4 | 7 | 8 |10 |
  0   1   2  [3] 4   5
              ↑
            High move here

Iteration 3:
  low=3, high=3
  mid = (3+3)/2 = 3
  nums[3] = 7
  
  7 >= 5? YES! ✓
  └─ ans = 7 (better answer! 8 > 7)
  └─ high = 3 - 1 = 2
  
  Status: Answer update karey (7 < 8)
          Continue search LEFT

Iteration 4:
  low=3, high=2
  low > high → LOOP ENDS
  
RETURN ans = 7 ✓

Trace:
  ans: -1 → 8 → 7
  Smallest >= 5 = 7 ✓
```

---

## 📊 Dry Run Example 2: Floor

```
Array: [3, 4, 4, 7, 8, 10]
Target: 5

FLOOR SEARCH:

Initial State:
  low=0, high=5, ans=-1
  Target: <= 5 dhundo (largest)

|---|---|---|---|---|---|
| 3 | 4 | 4 | 7 | 8 |10 |
  0   1   2   3   4   5

Iteration 1:
  low=0, high=5
  mid = (0+5)/2 = 2
  nums[2] = 4
  
  4 <= 5? YES! ✓
  └─ ans = 4 (store kro!)
  └─ low = 2 + 1 = 3
  
  Status: Answer mil gaya (4), par RIGHT dekho
          Kya bada <= 5 hoga?

|---|---|---|---|---|---|
| 3 | 4 | 4 | 7 | 8 |10 |
  0   1   2  [3] 4   5
              ↑
            Low move here

Iteration 2:
  low=3, high=5
  mid = (3+5)/2 = 4
  nums[4] = 8
  
  8 <= 5? NO
  └─ high = 4 - 1 = 3
  
  Status: 8 bada hai, LEFT dekho
          Ans = 4 (still)

|---|---|---|---|---|---|
| 3 | 4 | 4 | 7 | 8 |10 |
  0   1   2  [3] 4   5
              ↑
            High move here

Iteration 3:
  low=3, high=3
  mid = (3+3)/2 = 3
  nums[3] = 7
  
  7 <= 5? NO
  └─ high = 3 - 1 = 2
  
  Status: 7 bada hai, LEFT dekho
          Ans = 4 (still)

Iteration 4:
  low=3, high=2
  low > high → LOOP ENDS
  
RETURN ans = 4 ✓

Trace:
  ans: -1 → 4
  Largest <= 5 = 4 ✓
```

---

## 🔄 Comparison: Ceil vs Floor

### Direction Logic Side-by-Side

```
                CEIL                    FLOOR
              ────────                ────────
Condition:    >= x                    <= x
Meaning:      Smallest >=             Largest <=

Valid Found?  
  ans = element                       ans = element
  high = mid - 1                      low = mid + 1
  Move LEFT!                          Move RIGHT!

Invalid:
  low = mid + 1                       high = mid - 1
  Move RIGHT!                         Move LEFT!

Why?
  Ceil: Smallest answer              Floor: Largest answer
        LEFT mein dekho                      RIGHT mein dekho
        (smaller candidates)                 (larger candidates)

Pattern:
  >= → LEFT (smaller answer)
  <= → RIGHT (larger answer)

Memory Trick:
  CEIL = "Upstairs" = >= = Go LEFT to find smallest
  FLOOR = "Downstairs" = <= = Go RIGHT to find largest
```

---

## 🎓 Pattern Recognition

### Ye Problem Types Recognize Karo

#### Pattern 1: **Exact Element vs Boundary Element**

```
Exact Match:
  Target found → Stop immediately
  Example: Binary Search, Search in Array

Boundary/Position:
  Target na ho toh close-to-target element
  Example: Floor, Ceil, Lower Bound, Upper Bound
```

#### Pattern 2: **Direction After Valid Answer**

```
Smallest >= x (Ceil):    Valid mila → LEFT ← (smaller)
Largest <= x (Floor):    Valid mila → RIGHT → (larger)
First >= x (Lower Bound): Valid mila → LEFT ← (first)
Last <= x (Floor):       Valid mila → RIGHT → (last)

Rule: Direction decide karey answer type se!
```

#### Pattern 3: **Search Space Thinking**

```
Before: [1, 2, 3, 4, 7, 8, 9, 10]
Target: 5

Question:
├─ Smallest >= 5? → Ceil → 7 (RIGHT element)
├─ Largest <= 5? → Floor → 4 (LEFT element)
└─ Can I find both in one search? → NO! (separate logic)

Intuition: >= opposite direction hai <=
          Dono separate searches!
```

---

## 🎯 Edge Cases & Handling

### Edge Case 1: Target Array se Smaller

```
Array: [5, 7, 8, 10]
Target: 3

Ceil(3):
  - Smallest >= 3? 5
  - Return 5 ✓

Floor(3):
  - Largest <= 3? Nothing
  - Return -1 ✓

Trace:
  Ceil: 5>=3 mil gaya pehle hi
  Floor: <= kabhi true nahi hua
```

### Edge Case 2: Target Array se Larger

```
Array: [1, 3, 5, 7]
Target: 10

Ceil(10):
  - Smallest >= 10? Nothing
  - Return -1 ✓

Floor(10):
  - Largest <= 10? 7
  - Return 7 ✓

Trace:
  Ceil: >= kabhi true nahi hua
  Floor: 7<=10 mil gaya (aur continue)
```

### Edge Case 3: Exact Match

```
Array: [1, 3, 5, 7]
Target: 5

Ceil(5):
  - Smallest >= 5? 5 itself
  - Return 5 ✓

Floor(5):
  - Largest <= 5? 5 itself
  - Return 5 ✓

Trace:
  Dono same answer (element itself)
```

### Edge Case 4: Duplicates

```
Array: [3, 3, 3, 5, 7]
Target: 3

Ceil(3):
  - Smallest >= 3? 3 (pehla wala)
  - Return 3 ✓
  - (LEFT jaoge, pehla 3 mil jaega)

Floor(3):
  - Largest <= 3? 3 (last wala)
  - Return 3 ✓
  - (RIGHT jaoge, last 3 tak pohoch jaoge)

Trace:
  Ceil finds FIRST >= (leftmost)
  Floor finds LAST <= (rightmost)
```

### Edge Case 5: Single Element

```
Array: [5]
Target: 5

Ceil(5): 5 ✓
Floor(5): 5 ✓

Array: [5]
Target: 3

Ceil(3): 5 (only >= option)
Floor(3): -1 (no <= option)
```

---

## 🎤 Interview Signals & Tips

### Interviewer Puchega: "Kyun Alag Alag Search?"

**Your Answer:**
```
"Floor aur Ceil dono mein condition alag hain:
- Ceil: >= (smallest)
- Floor: <= (largest)

Aur direction bhi opposite hain:
- Ceil: Valid mila → LEFT (chhota chahiye)
- Floor: Valid mila → RIGHT (bada chahiye)

Toh ek hi loop mein combine nahi kar sakte!
Alag alag search karna padta hai."
```

### Interviewer Puchega: "High = n-1 vs High = n?"

**Your Answer:**
```
"Yahan HIGH = n-1 hai kyunki:
- Array ke indices 0 to n-1 tak hain
- Element jo -1 nahi dena (nahi mil gaya case)
- Toh n-1 se start karo, out of bounds nahi jayega"
```

### Interviewer Puchega: "Kyun Answer Store + Continue?"

**Your Answer:**
```
"Kyunki hum boundary dhund rahe hain, exact match nahi.

Example: Ceil for 5 in [1,3,7,9]
- 7 >= 5? YES, store 7
- Par chhota >= 5 ho sakta hai?
- Search continue karo...
- Nahi mila toh 7 hi answer!

Ye 'valid answer + continue search' pattern hai
boundary problems mein."
```

### Interviewer Puchega: "Time Complexity?"

**Your Answer:**
```
"O(log n) kyunki:
- Ek search mein n/2 → n/4 → ... → 1
- Ek element take pata chalega
- Two searches = O(log n) + O(log n) = O(log n)

(Constants matter nahi asymptotically)"
```

---

## 🚨 Common Mistakes (Interview mein avoid!)

### Mistake 1: Floor aur Ceil Condition Mix-Up

```
❌ WRONG:
FLOOR:
  if nums[mid] >= x:     // Ceil condition use kar diya!
    floor = nums[mid]
    low = mid + 1

✓ CORRECT:
FLOOR:
  if nums[mid] <= x:     // Correct condition
    floor = nums[mid]
    low = mid + 1
```

### Mistake 2: Direction Backwards

```
❌ WRONG:
CEIL:
  if nums[mid] >= x:
    ans = nums[mid]
    low = mid + 1         // RIGHT gaya! Backwards!

✓ CORRECT:
CEIL:
  if nums[mid] >= x:
    ans = nums[mid]
    high = mid - 1        // LEFT jao (smaller >= needed)
```

### Mistake 3: Answer Store Karne Ke Baad Immediately Return

```
❌ WRONG:
if nums[mid] >= x:
  return nums[mid]       // Immediately return!
  
(Kya guarantee pehla valid answer
 sabse chhota >= hai?)

✓ CORRECT:
if nums[mid] >= x:
  ans = nums[mid]        // Store kro
  high = mid - 1         // Continue search (chhota chahiye)
```

### Mistake 4: Low/High Reset Na Karey Second Search Mein

```
❌ WRONG:
// CEIL search
low = 0, high = n-1
... search ...

// FLOOR search (WITHOUT reset!)
// low = 0, high = n-1    // Forgot this!
... search ...

✓ CORRECT:
// CEIL search
low = 0, high = n-1
... search ...

// FLOOR search (RESET!)
low = 0, high = n-1      // Reset karna zaroori!
... search ...
```

### Mistake 5: Confusing Exact Match with Boundary

```
❌ WRONG:
if nums[mid] == x:
  return nums[mid]       // Ye exact match logic hai!

(Boundary logic nahi!)

✓ CORRECT:
if nums[mid] <= x:
  ans = nums[mid]        // Valid answer, but continue
  low = mid + 1          // Aur bada <= dhundo
```

### Mistake 6: Not Tracking Answer Variable in Dry Run

```
❌ WRONG DRY RUN:
Iteration 1: mid=2, nums[2]=4, 4<=5? YES, low=3
Iteration 2: mid=4, nums[4]=8, 8<=5? NO, high=3
...
(Confusing! Kyun low/high badal rahe ho?)

✓ CORRECT DRY RUN:
Iteration 1: mid=2, nums[2]=4
  4<=5? YES → ans=4 (store!)
  low=3 (RIGHT dekho bada answer)

Iteration 2: mid=4, nums[4]=8
  8<=5? NO → high=3 (LEFT dekho)
  ans=4 (unchanged)

(Clear! Answer track ho rahe ho!)
```

### Mistake 7: Using `low = mid - 1` in Ceil

```
❌ WRONG:
CEIL:
  if nums[mid] >= x:
    ans = nums[mid]
    low = mid - 1         // Ye floor logic hai!

✓ CORRECT:
CEIL:
  if nums[mid] >= x:
    ans = nums[mid]
    high = mid - 1        // Ceil logic
```

---

## 📝 Revision Notes (Quick Summary)

### Floor aur Ceil: Side-by-Side

```
CEIL (Ceiling):
├─ Definition: Smallest >= x
├─ Condition: if nums[mid] >= x
├─ Direction: high = mid - 1 (LEFT)
├─ Why LEFT: Chhota valid answer chahiye
└─ Returns: ans (smallest >=) or -1

FLOOR (Floor):
├─ Definition: Largest <= x
├─ Condition: if nums[mid] <= x
├─ Direction: low = mid + 1 (RIGHT)
├─ Why RIGHT: Bada valid answer chahiye
└─ Returns: ans (largest <=) or -1

KEY: >= aur <= opposite hain, direction bhi opposite!
```

### Answer Variable Key Role

```
WHY ANSWER VARIABLE?

Without:
- Loop karte karte confusing ho jata hai
- Kyun high/low badal rahe ho?
- Goal kyun clear nahi?

With:
- Valid condition mila → ans update
- Invalid → Search direction
- Loop ends → ans return (sab se baad valid)

Pattern:
  if CONDITION:
    ans = STORE
    DIRECTION = OPPOSITE    (smaller/larger chahiye)
  else:
    OPPOSITE_DIRECTION = OPPOSITE
```

### Search Strategy

```
Step 1: Problem padho (Floor ya Ceil?)
Step 2: Condition fix karo (<= ya >=?)
Step 3: Direction fix karo (LEFT ya RIGHT?)
Step 4: Dry run karo (ans track karte hue)
Step 5: Edge cases test karo
```

---

## 🔗 Related Problems

1. **Lower Bound** → Similar ">=" condition (Ceil jaise)
2. **Upper Bound** → Similar ">" condition
3. **First Bad Version** → Binary search on answer
4. **Find K Closest Elements** → Floor + Ceil use
5. **Median of Two Sorted Arrays** → Floor + Ceil combine

---

## 📊 Comparison Table: Decision Making

```
When to Use What?

Problem:              Element Type:     Condition:   Direction:
─────────────────────────────────────────────────────────────
Ceil (Smallest >=)    Found >= x        >= x         LEFT
Floor (Largest <=)    Found <= x        <= x         RIGHT
Lower Bound           First >= x        >= x         LEFT
Upper Bound           First > x         > x          LEFT
Search Insert         Position of x     >= x         LEFT

Pattern: 
- Smallest answer → >= → LEFT
- Largest answer → <= → RIGHT
```

---

## ✅ Self-Check Checklist

- [ ] Ceil = Smallest >=? (Hindi: x se bada ya barabar sabse chhota)
- [ ] Floor = Largest <=? (Hindi: x se chhota ya barabar sabse bada)
- [ ] Ceil direction = LEFT? (Chhota >=)
- [ ] Floor direction = RIGHT? (Bada <=)
- [ ] Answer variable track karte dry run?
- [ ] Dono search separate (reset low/high)?
- [ ] Edge cases: target > last, target < first, exact match?
- [ ] Common mistakes: Condition/Direction/Immediate return?
- [ ] Time complexity O(log n) intuition?

---

## 🎯 Final Pattern Summary

### Boundary Search Intuition

```
EXACT MATCH SEARCH (Normal Binary Search):
  Find element → Stop immediately
  Either found or not found!

BOUNDARY SEARCH (Floor/Ceil):
  Find closest/boundary element
  Valid answer store kro, par search continue
  Aur better (smallest/largest) answer dhundo!

Floor/Ceil = Boundary Search
├─ Ceil: Boundary = "Smallest >=
├─ Floor: Boundary = "Largest <="
└─ Pattern: >= opposite hai <=
```

### Direction Logic Intuition

```
GOAL: Smallest something?
  → Valid mila → LEFT jao
  
GOAL: Largest something?
  → Valid mila → RIGHT jao

Ceil: Smallest >=  → LEFT ← (chhota chahiye)
Floor: Largest <=  → RIGHT → (bada chahiye)
```

---

**Happy Learning! Floor aur Ceil clear ho gaye! 🚀**
