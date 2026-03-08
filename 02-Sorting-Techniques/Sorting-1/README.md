# 📘 Sorting Intuition – Bubble vs Selection vs Insertion

This page captures the **core thinking patterns** behind the three fundamental sorting algorithms.

Goal:

```text
Understand HOW elements move inside the array.
```

Once you remember the **movement pattern**, the algorithm becomes impossible to forget.

---

# 1️⃣ Bubble Sort Intuition

Core idea:

```text
Push the largest element to the end in each pass.
```

Mechanism:

```text
Compare adjacent elements
Swap if order is wrong
```

Example

```
[7,4,1,5,3]

Pass 1
[4,1,5,3,7]

Pass 2
[1,4,3,5,7]

Pass 3
[1,3,4,5,7]
```

Movement pattern:

```text
Large elements bubble to the right.
```

Key observation:

```
Right side becomes sorted.
```

Memory anchor:

```
Compare → Swap → Largest moves right
```

---

# 2️⃣ Selection Sort Intuition

Core idea:

```text
Find the smallest element and place it at the correct position.
```

Mechanism:

```text
Search minimum
Swap with current position
```

Example

```
[7,4,1,5,3]

Pass 1
[1,4,7,5,3]

Pass 2
[1,3,7,5,4]

Pass 3
[1,3,4,5,7]
```

Movement pattern:

```text
Smallest element jumps to the front.
```

Key observation:

```
Left side becomes sorted.
```

Memory anchor:

```
Find Minimum → Place at Front
```

---

# 3️⃣ Insertion Sort Intuition

Core idea:

```text
Insert each element into its correct position in the sorted part.
```

Mechanism:

```text
Take element
Shift larger elements
Insert element
```

Example

```
[7,4,1,5,3]

Step 1
[4,7]

Step 2
[1,4,7]

Step 3
[1,4,5,7]
```

Movement pattern:

```text
Elements shift right to create space.
```

Key observation:

```
Sorted portion grows from the left.
```

Memory anchor:

```
Shift → Insert
```

---

# 4️⃣ Element Movement Comparison

| Algorithm      | Element Movement                |
| -------------- | ------------------------------- |
| Bubble Sort    | Large elements move right       |
| Selection Sort | Smallest element jumps to front |
| Insertion Sort | Elements shift to insert key    |

---

# 5️⃣ Swap vs Shift

| Algorithm      | Operation         |
| -------------- | ----------------- |
| Bubble Sort    | Multiple swaps    |
| Selection Sort | One swap per pass |
| Insertion Sort | Shifting elements |

Important insight:

```
Insertion sort shifts instead of swapping.
```

---

# 6️⃣ When Each Algorithm Works Best

| Algorithm      | Best Scenario           |
| -------------- | ----------------------- |
| Bubble Sort    | Rarely used in practice |
| Selection Sort | Minimum swaps required  |
| Insertion Sort | Nearly sorted arrays    |

Important observation:

```
Insertion Sort is fastest when array is almost sorted.
```

---

# 7️⃣ Time Complexity Comparison

| Algorithm | Best  | Average | Worst |
| --------- | ----- | ------- | ----- |
| Bubble    | O(n²) | O(n²)   | O(n²) |
| Selection | O(n²) | O(n²)   | O(n²) |
| Insertion | O(n)  | O(n²)   | O(n²) |

Reason:

```
Insertion sort shifts only when needed.
```

---

# 8️⃣ Mental Shortcut (Most Important)

If you forget algorithms, remember this:

```
Bubble Sort → Push largest to end
Selection Sort → Pick smallest to front
Insertion Sort → Insert element in sorted part
```

Once the **movement idea** is clear, the code becomes easy to reconstruct.

---

# 🎯 One-Line Summary

```
Bubble Sort → Adjacent swapping
Selection Sort → Minimum selection
Insertion Sort → Element insertion
```

---
