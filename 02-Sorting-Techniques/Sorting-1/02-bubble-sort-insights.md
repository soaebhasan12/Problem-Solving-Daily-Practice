# 📘 Bubble Sort – Key Insights

## 1️⃣ Core Idea

Bubble Sort repeatedly **compares adjacent elements** and swaps them if they are in the wrong order.

Memory anchor:

```
Compare → Swap → Largest bubbles to end
```

Har pass me **largest element rightmost position par settle ho jata hai**.

---

# 2️⃣ Algorithm Intuition

Array ko algorithm gradually divide karta hai:

```
Left  → Unsorted
Right → Sorted
```

Example

```
[7,4,1,5,3]

Pass 1
[4,1,5,3] | [7]

Pass 2
[1,4,3] | [5,7]

Pass 3
[1,3] | [4,5,7]
```

Right side me **sorted part grow hota hai**.

---

# 3️⃣ Loop Structure (Important)

Outer loop:

```
n - 1 passes
```

Reason:

```
After each pass, one largest element reaches its correct position.
```

Inner loop:

```
len(nums) - i - 1
```

Reason:

```
Last i elements already sorted.
```

---

# 4️⃣ Swap Condition

Swap tab hota hai jab order galat ho:

```
if nums[j] > nums[j+1]
```

Meaning:

```
left element bigger than right → swap
```

---

# 5️⃣ Comparison Pattern

Comparisons gradually reduce:

```
Pass 1 → n-1
Pass 2 → n-2
Pass 3 → n-3
...
Pass n-1 → 1
```

Total comparisons:

```
O(n²)
```

---

# 6️⃣ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n²)      |
| Average | O(n²)      |
| Worst   | O(n²)      |

Reason:

```
Basic bubble sort always performs full passes.
```

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

| Property | Value                |
| -------- | -------------------- |
| Stable   | ✅ Yes                |
| In-place | ✅ Yes                |
| Adaptive | ❌ No (basic version) |

---

# 9️⃣ Common Beginner Mistakes

1️⃣ Starting inner loop from wrong index
2️⃣ Wrong loop boundary causing index error
3️⃣ Comparing wrong elements (`j+1` misuse)
4️⃣ Forgetting adjacent comparison logic

Correct mental pattern:

```
compare nums[j] and nums[j+1]
swap if left > right
```

---

# 🔟 Memory Shortcut

```
Bubble Sort =
Push Largest Element to End Every Pass
```

Or simply:

```
Compare Adjacent → Swap → Repeat
```

---

# 🎯 One-Line Interview Explanation

Bubble sort repeatedly **compares adjacent elements and swaps them if they are in the wrong order**, causing the largest element in each pass to bubble up to the end of the array.

---
