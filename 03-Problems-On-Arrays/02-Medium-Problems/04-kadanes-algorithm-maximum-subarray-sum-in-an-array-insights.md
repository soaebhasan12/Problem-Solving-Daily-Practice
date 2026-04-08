# 📄 Kadane’s Algorithm (Maximum Subarray Sum) Insights

---

## 🧠 Problem Understanding

Given array `nums`:

👉 Find:

```text id="n1a2s3"
maximum sum of any subarray
```

👉 Subarray:

```text id="m2b3c4"
continuous elements
```

---

## 🔍 Problem Classification

👉 Signals:

* Subarray
* Maximum / Minimum
* Sum

👉 Possible approaches:

```text id="k2l3m4"
Brute Force / Optimization / Kadane
```

---

# ⚙️ Approach 1: Brute Force (Generate Subarrays)

## 💡 Idea

```text id="b1c2d3"
Generate all subarrays
→ calculate sum
→ track max
```

---

## 🧠 Pseudo Code

```text id="p1q2r3"
for start in range(n):
    for end in range(start, n):
        curr_sum = 0
        for k in range(start, end+1):
            curr_sum += nums[k]
        max_sum = max(max_sum, curr_sum)
```

---

## 🔥 Dry Run

```text id="d1e2f3"
nums = [2,3]
```

Subarrays:

```text id="g1h2i3"
[2] → 2
[2,3] → 5
[3] → 3
```

👉 max = 5

---

## ⏱️ Complexity

```text id="t1u2v3"
Time → O(n³)
```

---

## 🚫 Problem

* Too slow
* Repeated sum calculation ❌

---

# ⚡ Approach 2: Better (Carry Forward Sum)

## 💡 Idea

```text id="o1p2q3"
curr_sum reuse karo
→ previous sum + next element
```

---

## 🧠 Pseudo Code

```text id="r1s2t3"
for start in range(n):
    curr_sum = 0
    for end in range(start, n):
        curr_sum += nums[end]
        max_sum = max(max_sum, curr_sum)
```

---

## 🔥 Dry Run

```text id="u1v2w3"
nums = [2,3,5]
```

```text id="x1y2z3"
start=0:
2 → 5 → 10

start=1:
3 → 8

start=2:
5
```

---

## ⏱️ Complexity

```text id="a2b3c4"
Time → O(n²)
```

---

# 🚀 Approach 3: Kadane’s Algorithm (Optimal)

## 💡 Core Idea

```text id="k1a2d3"
Negative prefix ko discard karo
```

👉 Agar sum negative ho gaya:

```text id="l2m3n4"
uska future me koi use nahi ❌
```

---

## 🧠 Pseudo Code

```text id="z1x2c3"
currSum = 0
maxSum = nums[0]

for each element:
    currSum += element
    maxSum = max(maxSum, currSum)

    if currSum < 0:
        currSum = 0
```

---

## 🔥 Dry Run (VERY IMPORTANT ⭐)

```text id="q1w2e3"
nums = [2,3,5,-2,7,-4]
```

---

### Step-by-step:

```text id="r4t5y6"
2 → curr=2, max=2
3 → curr=5, max=5
5 → curr=10, max=10
-2 → curr=8, max=10
7 → curr=15, max=15
-4 → curr=11, max=15
```

👉 Final:

```text id="u7i8o9"
maxSum = 15
```

---

## ⏱️ Complexity

```text id="p0o9i8"
Time → O(n)
Space → O(1)
```

---

# ⚠️ Your Mistakes (VERY IMPORTANT 🚨)

## ❌ Mistake 1: Wrong max function

```text id="z9x8c7"
math.max ❌
```

👉 Correct:

```text id="b6n5m4"
max() ✅
```

---

## ❌ Mistake 2: max_sum initialization

```text id="a1s2d3"
max_sum = 0 ❌
```

👉 Negative arrays fail ho jayenge

✔️ Correct:

```text id="f4g5h6"
max_sum = nums[0]
```

---

## ❌ Mistake 3: Wrong comparison

```text id="j7k8l9"
if max_sum > curr_sum:
    max_sum = curr_sum ❌
```

👉 Reverse ho gaya logic

✔️ Correct:

```text id="m0n1b2"
max_sum = max(max_sum, curr_sum)
```

---

## ❌ Mistake 4: Subarray logic confusion

👉 start/end/k roles clear nahi the ❌

---

# 🔁 Future Mistakes (1 Month Later 🚩)

👉 Tu yeh galti karega:

* ❌ currSum reset bhool jayega
* ❌ negative case handle nahi karega
* ❌ max update ka order galat karega
* ❌ brute vs Kadane confuse karega

---

# 🧠 Memory Tricks

```text id="x9c8v7"
Negative → reset
Positive → carry forward
```

---

# 🚩 Interview Signals

👉 Agar interviewer bole:

* “maximum subarray sum”
* “optimize to O(n)”

👉 Direct signal:

```text id="q3w4e5"
Kadane’s Algorithm 🔥
```

---

# 🎯 Comparison Table

| Approach | Time | Idea             |
| -------- | ---- | ---------------- |
| Brute    | n³   | generate all     |
| Better   | n²   | carry sum        |
| Kadane   | n    | discard negative |

---

# 📘 Revision Points

* Subarray → continuous
* Repeated sum → optimize
* Negative prefix discard
* Kadane = greedy thinking

---

# 🎤 Interview Answer (Short)

👉 “We use Kadane’s Algorithm to find maximum subarray sum in O(n) time by discarding negative prefixes and keeping track of current and global maximum.”

---

# 🧠 FINAL SUMMARY

* Brute → slow
* Better → improved
* Kadane → best
* Core idea = discard negative 🔥

---

# 🚀 Next Thinking

👉 Agar subarray bhi return karna ho (indices)…

👉 Kadane ko kaise modify karoge? 🤔

👉 Soch — next level question hai 😏
