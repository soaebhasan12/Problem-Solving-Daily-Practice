# 📘 Recursion for Absolute Beginners
# 🚀 What You Will Learn

- What recursion actually means
- Why base case is mandatory
- How recursive calls work in memory
- Down phase vs Up phase
- How return values travel in the call stack
- How to think mathematically before coding

---

# 🧠 What is Recursion?

Recursion is when a function calls itself
to solve a smaller version of the same problem.

Example:

Sum of first 3 numbers:

3 + 2 + 1

Mathematically:

sum(3) = 3 + sum(2)
sum(2) = 2 + sum(1)
sum(1) = 1 + sum(0)
sum(0) = 0

This breakdown is recursion.

---

# 🔥 Two Golden Rules

## 1️⃣ Base Case

Stopping condition.
Without it → infinite function calls → Stack Overflow Error.

## 2️⃣ Reduction Step

Each call must move closer to base case.

n → n-1
5 → 4 → 3 → 2 → 1 → 0

If problem size does not reduce, recursion never ends.

---

# 📦 What Happens Behind the Scenes?

When a function calls itself:

The previous function does NOT disappear.

It waits inside memory.
This memory structure is called the **Call Stack**.

Example:

fun(3)
→ fun(2)
→ fun(1)
→ fun(0)

Stack builds downward.

When base case is reached,
stack starts resolving upward.

This creates two phases:

- Down Phase (stack building)
- Up Phase (calculation happens)

---

# ⬇️ Down Phase vs ⬆️ Up Phase

If code is:

```python
print(n)
test(n-1)
```

Print happens during down phase.

If code is:

```python
test(n-1)
print(n)
```

Print happens during up phase.

Golden Rule:

- Code before recursive call → executes going down
- Code after recursive call → executes coming up

---

# 🔁 Return Value Flow

Example:

```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
```

For n = 3:

Down phase creates:

3 + ?
2 + ?
1 + ?
0

Up phase calculates:

1 + 0 = 1
2 + 1 = 3
3 + 3 = 6

Final Answer = 6

Important:

Base case does not just stop recursion.
It defines the starting value of the final answer.

---

# ⚠️ Common Beginner Mistakes

- Forgetting base case
- Wrong base condition
- Not reducing input
- Calling function without modifying argument
- Not understanding stack behavior

---

# ⏳ Time Complexity (Linear Recursion)

For n calls:

fun(n)
fun(n-1)
fun(n-2)
...
fun(0)

Total calls ≈ n

Time Complexity: O(n)

This is linear recursion (single branch).

---

# 📝 Memory Version (Quick Revision)

Recursion Template:

```python
def func(n):
    if base_case:
        return value

    return work + func(smaller_input)
```

Checklist for every problem:

- What is base case?
- How is problem reducing?
- Is work happening in down phase or up phase?
- What does base case return?
---










**LeetCode FREE questions**

🟥 Must Revise (Very Important)
🟧 Important
🟨 Good Practice
🟩 Optional (After confidence)

---

# 🟥 MUST REVISE (Foundation Strong Karne Ke Liye)

1️⃣ **509. Fibonacci Number**
→ Classic recursion + exponential tree samajhne ke liye

2️⃣ **70. Climbing Stairs**
→ Fibonacci pattern detect karna seekho

3️⃣ **344. Reverse String**
→ Two pointer + recursion combination

4️⃣ **206. Reverse Linked List**
→ Interview favourite recursion question

5️⃣ **21. Merge Two Sorted Lists**
→ Real recursive thinking develop karta hai

---

# 🟧 IMPORTANT (Pattern Recognition)

6️⃣ **231. Power of Two**
→ Simple base case clarity

7️⃣ **50. Pow(x, n)**
→ Fast recursion thinking (divide & conquer intro)

8️⃣ **104. Maximum Depth of Binary Tree**
→ Tree recursion ka entry point

9️⃣ **226. Invert Binary Tree**
→ Recursive swapping (tree version of reverse array)

---

# 🟨 GOOD PRACTICE (Logic Stretch)

🔟 **101. Symmetric Tree**
→ Two side recursive comparison

1️⃣1️⃣ **112. Path Sum**
→ Recursive decision making

1️⃣2️⃣ **404. Sum of Left Leaves**
→ Condition + recursion combination

---

# 🟩 OPTIONAL (After Confidence)

1️⃣3️⃣ **24. Swap Nodes in Pairs**
→ Linked list recursion tricky but good

1️⃣4️⃣ **95. Unique Binary Search Trees II**
→ Advanced recursion (skip for now)

---

# 🎯 How You Should Practice

For each question:

1. First solve using brute logic
2. Then recursive thinking
3. Draw recursion tree
4. Identify:

   * Base case
   * Reduction
   * Work position
   * Time complexity shape

---

If I had to choose TOP 5 for placement revision:

1. Fibonacci
2. Climbing Stairs
3. Reverse Linked List
4. Maximum Depth of Binary Tree
5. Merge Two Sorted Lists

---