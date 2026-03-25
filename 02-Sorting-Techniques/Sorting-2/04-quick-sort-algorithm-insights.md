# Quick Sort Algorithm Insights

---

## 1️⃣ Core Idea (Intuition)

```text
Pick a pivot → place it at correct position → recursively sort left & right
```

Memory line:

```text
Partition → Fix Pivot → Recurse
```

---

## 2️⃣ Element Movement (Visualization)

Example:

```text
[7,4,1,5,3]
pivot = 3
```

After partition:

```text
[1] + [3] + [7,4,5]
```

Then:

```text
[7,4,5] → pivot = 5 → [4] + [5] + [7]
```

Final:

```text
[1,3,4,5,7]
```

---

## 3️⃣ Partition Logic (Heart of Algorithm)

Maintain:

```text
i → last index of smaller elements
j → scanning pointer (left → right)
pivot → last element
```

Rule:

```text
if nums[j] <= pivot:
    i++
    swap(nums[i], nums[j])
```

Final step:

```text
swap(nums[i+1], pivot)
```

---

## 4️⃣ Partition Invariant (VERY IMPORTANT)

During loop:

```text
[start → i] → elements ≤ pivot
[i+1 → j] → unknown
[end] → pivot
```

After loop:

```text
pivot placed at index = i+1 (correct position)
```

---

## 5️⃣ Recursive Structure

```text
quickSort(nums, start, end):

    partition → pivot_index

    quickSort(left part)
    quickSort(right part)
```

Actual:

```text
left  = start → pivot_index-1
right = pivot_index+1 → end
```

---

## 6️⃣ Base Case

```text
if start >= end:
    stop
```

Reason:

```text
0 or 1 element → already sorted
```

---

## 7️⃣ Time Complexity (Intuition Based)

### Best Case

```text
balanced split every time
```

```text
T(n) = 2T(n/2) + n
→ O(n log n)
```

---

### Worst Case ⚠️

```text
already sorted / reverse sorted
pivot = smallest or largest
```

```text
T(n) = T(n-1) + n
→ O(n²)
```

---

### Average Case

```text
random distribution
→ O(n log n)
```

---

## 8️⃣ Space Complexity

```text
O(log n) → recursion stack (best/avg)
O(n) → worst case (skewed recursion)
```

---

## 9️⃣ Properties

| Property         | Value |
| ---------------- | ----- |
| Stable           | ❌ No  |
| In-place         | ✅ Yes |
| Adaptive         | ❌ No  |
| Divide & Conquer | ✅ Yes |

---

## 🔟 Pattern Recognition (Interview Signals)

Use Quick Sort when:

```text
large dataset
in-place sorting needed
average performance matters
```

Avoid when:

```text
already sorted data (if pivot fixed)
stability required
```

---

## 1️⃣1️⃣ Common Mistakes

### ❌ Mistake 1

```text
i not incremented before swap
```

---

### ❌ Mistake 2

```text
pivot swap wrong index
(correct = i+1)
```

---

### ❌ Mistake 3

```text
wrong recursion range
```

---

### ❌ Mistake 4

```text
start/end not handled (in LeetCode style)
```

---

## 1️⃣2️⃣ Teaching Explanation

Explain as:

```text
Divide array using pivot
Place pivot at correct position
Solve left and right independently
```

Analogy:

```text
pivot = boundary maker
```

---

## 1️⃣3️⃣ Memory Trick

```text
Scan → Swap → Place Pivot → Recurse
```

---

## 1️⃣4️⃣ Final Insight

```text
Quick Sort efficiency depends on partition balance
```

Key:

```text
Good pivot → O(n log n)
Bad pivot → O(n²)
```

---

## 1️⃣5️⃣ Code Mapping (Your Implementation)

```text
pivot = nums[end]
i = start - 1
j = start → end-1
swap when <= pivot
pivot placed at i+1
left recursion → start to i
right recursion → i+2 to end
```

---

## ✅ Conclusion

```text
Quick Sort =
Partition-based sorting
Fast in practice
Worst-case sensitive
```

---
