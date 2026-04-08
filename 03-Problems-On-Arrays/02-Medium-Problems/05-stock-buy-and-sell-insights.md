🔥 Bhai yeh bhi **top interview problem hai 💯 (Kadane cousin 😏)**
---

# 📄 Best Time to Buy and Sell Stock Insights

## 🧠 Problem Understanding

Given array `arr`:

```text id="a1b2c3"
arr[i] = stock price on day i
```

👉 Task:

```text id="d4e5f6"
Max profit find karo (buy once, sell once)
```

---

## ⚠️ Important Constraint

```text id="g7h8i9"
Buy before Sell hona chahiye
```

---

## 🔍 Problem Classification

👉 Signals:

* Profit maximize
* Future vs past comparison
* Single transaction

👉 Pattern:

```text id="j1k2l3"
Greedy / Kadane-type thinking
```

---

# ⚙️ Approach 1: Brute Force

## 💡 Idea

```text id="m4n5o6"
Har buy day ke liye
→ future me best sell day check karo
```

---

## 🧠 Pseudo Code

```text id="p7q8r9"
for i in range(n):
    for j in range(i+1, n):
        profit = arr[j] - arr[i]
        maxProfit = max(maxProfit, profit)
```

---

## ⏱️ Complexity

```text id="s1t2u3"
Time → O(n²)
```

---

## 🚫 Problem

* Slow
* Repeated comparisons ❌

---

# ⚡ Approach 2: Optimal (Greedy)

## 💡 Core Idea

```text id="v4w5x6"
Minimum price track karo (best buy)
→ aur har step pe max profit update karo
```

---

## 🧠 Pseudo Code

```text id="y7z8a9"
bestBuy = arr[0]
maxProfit = 0

for each price:
    if price > bestBuy:
        profit = price - bestBuy
        update maxProfit

    update bestBuy = min(bestBuy, price)
```

---

## 🔥 Dry Run (VERY IMPORTANT ⭐)

```text id="b1c2d3"
arr = [10, 7, 5, 8, 11, 9]
```

---

### Step-by-step:

```text id="e4f5g6"
10 → bestBuy=10

7 → bestBuy=7

5 → bestBuy=5

8 → profit=3 → max=3

11 → profit=6 → max=6

9 → profit=4 → max=6
```

👉 Final:

```text id="h7i8j9"
maxProfit = 6
```

---

## ⏱️ Complexity

```text id="k1l2m3"
Time → O(n)
Space → O(1)
```

---

# 🧠 Core Insight (Golden Line)

```text id="n4o5p6"
“Har din check karo: agar aaj bechun toh best profit kya milega?”
```

---

# ⚠️ Beginner Mistakes (VERY IMPORTANT 🚨)

## ❌ Mistake 1: Max & Min alag-alag find karna

```text id="q7r8s9"
maxVal aur minVal independently find kiya ❌
```

👉 Problem:

```text id="t1u2v3"
minVal future me ho sakta hai (invalid buy)
```

---

## ❌ Mistake 2: Index validation baad me

```text id="w4x5y6"
pehle values nikali, baad me index check ❌
```

👉 Wrong approach

---

## ❌ Mistake 3: Nested loop overthinking

👉 Brute ko optimize nahi kiya ❌

---

# 🔁 Future Mistakes (1 Month Later 🚩)

👉 Tu likely yeh galti karega:

* ❌ bestBuy update bhool jayega
* ❌ current profit calculate nahi karega
* ❌ “buy before sell” violate karega
* ❌ Kadane se connect nahi karega

---

# 🧠 Memory Tricks

```text id="z7x6c5"
Min so far → best buy
Current - min → profit
```

---

# 🚩 Interview Signals

👉 Agar interviewer bole:

* “max profit”
* “buy once sell once”
* “optimize to O(n)”

👉 Direct signal:

```text id="v3b2n1"
Greedy / Kadane-style approach 🔥
```

---

# 🎯 Comparison Table

| Approach | Time | Idea      |
| -------- | ---- | --------- |
| Brute    | n²   | try all   |
| Optimal  | n    | track min |

---

# 📘 Revision Points

* Buy before sell
* Min track karo
* Profit = current - min
* Single pass solution

---

# 🎤 Interview Answer (Short)

👉 “We track the minimum price so far and calculate the profit for each day, updating the maximum profit in O(n) time.”

---

# 🧠 FINAL SUMMARY

* Brute → slow
* Greedy → best
* Kadane-like thinking
* Min tracking = key 🔥

---

# 🚀 Next Thinking

👉 Agar multiple transactions allowed ho…

👉 strategy kaise change hogi? 🤔

👉 Soch — next level problem 😏
