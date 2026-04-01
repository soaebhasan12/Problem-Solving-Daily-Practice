# 📝 `Single Number Insights`

---

# 1️⃣ 🧠 Core Idea

```text
Every element appears twice except one → find that unique element
```

👉 Important constraint:

```text
pairs cancel out → only one element remains
```

---

# 2️⃣ 🧩 Pattern Recognition

👉 Possible approaches:

```text
1. Hashing (frequency count)
2. Bit Manipulation (XOR trick 🔥)
```

---

# 3️⃣ 🟡 Approach 1: Hashing (Frequency Map)

## 🧠 Intuition

```text
Count frequency of each number
Return the number with freq = 1
```

---

## ⚙️ Code

```python
class Solution:
    def singleNumber(self, nums):
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key in freq:
            if freq[key] == 1:
                return key
```

---

## ⏱️ Complexity

```text
Time = O(n)
Space = O(n)
```

---

## ⚠️ Your Mistakes & Learnings

❌ Used index instead of value as key
✔ Always use actual element → `nums[i]`

---

❌ Used `()` instead of `[]` in dict
✔ Correct → `map_dict[key]`

---

❌ Tried `.value` in dict
✔ Correct → `map_dict[key]`

---

❌ Wrong initialization (`+=` without value)
✔ First time → `= 1`

---

❌ Iterated using range
✔ Use:

```text
for key in dict
```

---

# 4️⃣ 🟢 Approach 2: XOR (Optimal 🔥)

## 🧠 Intuition (VERY IMPORTANT)

👉 XOR properties:

```text
a ^ a = 0
a ^ 0 = a
```

---

## 💡 Key Insight

```text
pairs cancel out → only single element remains
```

---

## 🧪 Example

```text
[4,1,2,1,2]

Step:
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1^1) ^ (2^2)
= 4 ^ 0 ^ 0
= 4
```

---

## ⚙️ Code

```python
class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result
```

---

## ⏱️ Complexity

```text
Time = O(n)
Space = O(1) 🔥
```

---

# 5️⃣ 🧠 When to Use What?

| Approach | Use Case                              |
| -------- | ------------------------------------- |
| Hashing  | Easy to think, beginner-friendly      |
| XOR      | Interview optimized, memory efficient |

---

# 6️⃣ 🚩 Interview Signals

👉 Agar question me aaye:

* “every element appears twice except one”
* “find unique element”
* “optimize space”

👉 Think:

```text
XOR 🔥
```

---

# 7️⃣ 🎯 Memory Trick

```text
Duplicate → cancel
Unique → remains
```

---

# 8️⃣ 🧠 Final Summary

* Hashing → simple but extra space
* XOR → optimal and elegant
* Always understand WHY XOR works

---

# 💬 My Opinion

👉 This problem is:

🔥 **Bit manipulation entry point**

👉 Agar XOR samajh liya:

* missing number
* single number II
* bit tricks

sab easy ho jayega 🚀
