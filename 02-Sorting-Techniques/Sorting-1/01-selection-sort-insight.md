# 📘 Selection Sort — Key Insights (Quick Revision)

## 1️⃣ Core Idea

Selection Sort repeatedly **selects the smallest element** from the unsorted portion and places it at the correct position.

Memory anchor:

```
Scan → Select → Swap
```

---

# 2️⃣ Algorithm Intuition

Array ko algorithm 2 parts me divide karta hai:

```
Left  → Sorted
Right → Unsorted
```

Example

```
[7,4,1,5,3]

[1] | [4,7,5,3]
[1,3] | [7,5,4]
[1,3,4] | [5,7]
[1,3,4,5] | [7]
```

Har pass me **minimum element correct position par place hota hai**.

---

# 3️⃣ Algorithm Structure

```
for each position i:
    assume nums[i] is minimum

    search remaining array

    if smaller element found:
        update minimum

    swap minimum with position i
```

---

# 4️⃣ Key Variable

```
min_index = i
```

Meaning:

```
current element ko minimum assume kiya
```

Update rule:

```
if nums[j] < nums[min_index]:
    min_index = j
```

Isliye `min_index = j`.

Kyuki **new smaller element mil gaya**.

---

# 5️⃣ Swap Timing

Swap **inner loop ke baad** hota hai.

```
nums[i] ↔ nums[min_index]
```

Reason:

Pehle **true minimum find karna hota hai**.

---

# 6️⃣ Time Complexity

Comparisons:

```
(n-1) + (n-2) + ... + 1
```

Total:

```
O(n²)
```

Important:

```
Best  = O(n²)
Worst = O(n²)
```

Selection sort **always full scan karta hai**.

---

# 7️⃣ Space Complexity

```
O(1)
```

Reason:

```
In-place sorting
```

---

# 8️⃣ Properties

| Property | Value   |
| -------- | ------- |
| Stable   | ❌ No    |
| In-place | ✅ Yes   |
| Swaps    | Minimum |

Selection sort **minimum swaps** karta hai.

---

# 9️⃣ When NOT to Use Selection Sort

Avoid when:

```
Large arrays
Nearly sorted arrays
Stable sorting required
```

Better algorithms:

```
Insertion Sort
Merge Sort
Quick Sort
```

---

# 🔟 Common Beginner Mistakes

* 1️⃣ wrong inner loop range
* 2️⃣ swap inside inner loop
* 3️⃣ comparing `nums[j+1]`
* 4️⃣ wrong `min_index` initialization

Correct pattern:

```
min_index = i
compare nums[j] < nums[min_index]
swap after inner loop
```

---

# 🧠 Your Personal Weak Points (Observed)

During solving this problem:

* 1️⃣ Loop boundary mistakes (`len(nums)-1`)
* 2️⃣ Index confusion (`j+1`)
* 3️⃣ Swap timing confusion
* 4️⃣ Missing minimum tracking variable

These are **normal beginner DSA mistakes**.

---

# 🎯 One Line Interview Explanation

Selection sort repeatedly **selects the smallest element from the unsorted portion and places it at the correct position**, gradually growing the sorted part of the array.

---