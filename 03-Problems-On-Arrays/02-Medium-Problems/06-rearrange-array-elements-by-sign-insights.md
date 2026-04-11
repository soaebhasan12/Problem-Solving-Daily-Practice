# 📄 Rearrange Array Elements by Sign Insights


## 🧠 Problem Understanding

Given array `nums`:

👉 Conditions:

```text
1. Equal number of positive and negative elements (in main problem)
2. Alternate placement required
3. Start with positive element
4. Relative order maintain karna hai (stable)
```

---

## 🔍 Problem Classification

👉 Signals:

* Rearrangement problem
* Stability (order preserve)
* Alternate pattern

👉 Pattern:

```text
Two Pointer / Simulation / Greedy Placement
```

---

# ⚙️ Approach 1: Using Extra Arrays (Basic)

## 💡 Idea

```text
Positive aur negative elements separate karo
→ phir alternate merge karo
```

---

## 🧠 Pseudo Code

```text
pos = all positive elements
neg = all negative elements

for i in range(len(pos)):
    add pos[i]
    add neg[i]
```

---

## 🔥 Dry Run

```text
nums = [1, -1, -3, -4, 2, 3]

pos = [1, 2, 3]
neg = [-1, -3, -4]

result = [1, -1, 2, -3, 3, -4]
```

---

## ⏱️ Complexity

```text
Time → O(n)
Space → O(n)
```

---

## ⚠️ Beginner Mistakes 🚨

* ❌ Loop half array tak chalana (`n//2` confusion)
* ❌ Alternation me index misuse
* ❌ Relative order break kar dena
* ❌ pos/neg length mismatch handle na karna

---

# ⚡ Approach 2: Optimal (Index Placement)

## 💡 Core Idea

```text
Even index → positive
Odd index → negative
```

👉 Direct correct position pe place karo

---

## 🧠 Pseudo Code

```text
Initialize new array of size n

posIndex = 0
negIndex = 1

for each element:
    if positive:
        place at posIndex
        posIndex += 2
    else:
        place at negIndex
        negIndex += 2
```

---

## 🔥 Dry Run (VERY IMPORTANT ⭐)

```text
nums = [1, -1, -3, -4, 2, 3]
```

```text
Index:   0   1   2   3   4   5
Result: [1, -1, 2, -3, 3, -4]
```

---

## ⏱️ Complexity

```text
Time → O(n)
Space → O(n)
```

---

## 🧠 Core Insight (Golden Line)

```text
“Correct position pe directly place karo → swapping ki zarurat nahi”
```

---

## ⚠️ Beginner Mistakes 🚨

* ❌ Empty list me direct index assignment
* ❌ Array size initialize na karna
* ❌ posIndex / negIndex increment bhool jana
* ❌ sign check galat likhna (`<0` vs `>0`)

---

# 🚀 Approach 3: Unequal Pos/Neg Case

## 💡 Core Idea

```text
Alternate fill karo
→ jo elements bach jaaye → end me append karo
```

---

## 🧠 Pseudo Code

```text
pos = positives
neg = negatives

i = j = 0

while both available:
    add pos[i]
    add neg[j]
    i++, j++

add remaining elements
```

---

## 🔥 Dry Run

```text
nums = [1, 2, 3, -1, -2]

pos = [1,2,3]
neg = [-1,-2]

result = [1,-1,2,-2,3]
```

---

## ⏱️ Complexity

```text
Time → O(n)
Space → O(n)
```

---

## ⚠️ Beginner Mistakes 🚨

* ❌ Unequal case ignore kar dena
* ❌ Leftover elements drop kar dena
* ❌ Infinite loop (wrong condition)
* ❌ Index out of bounds

---

# 🧠 Memory Tricks

```text
Even → Positive
Odd → Negative
```

---

# 🚩 Interview Signals

👉 Agar interviewer bole:

* “alternate positive and negative”
* “maintain order”
* “in-place or optimized?”

👉 Direct signal:

```text
Index placement / Two pointer simulation 🔥
```

---

# 🎯 Comparison Table

| Approach | Time | Space | Idea                   |
| -------- | ---- | ----- | ---------------------- |
| Basic    | n    | n     | split + merge          |
| Optimal  | n    | n     | direct index placement |
| Unequal  | n    | n     | merge + leftover       |

---

# 📘 Revision Points

* Alternate pattern identify karo
* Stability maintain karni hai
* Index mapping important hai
* Edge case (unequal) handle karo

---

# 🎤 Interview Answer (Short)

👉 “We can solve this by placing positives at even indices and negatives at odd indices using an auxiliary array, ensuring order is preserved.”

---

# 🧠 FINAL SUMMARY

* Problem = rearrangement + stability
* Best approach = index placement
* Extra case = unequal handling
* Pattern recognition = key 🔥

---

# 🚀 Next Thinking

👉 Agar in-place karna ho (without extra array)…

👉 kaise karoge? 🤔

👉 Yeh thoda tricky hai — next level problem 😏
