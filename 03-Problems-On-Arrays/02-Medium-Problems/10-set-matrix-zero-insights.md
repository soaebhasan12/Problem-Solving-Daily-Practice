# 📄 10 - Set Matrix Zeroes Insights

## 🧠 Problem Understanding

👉 Given matrix:

```text
Agar kisi cell me 0 hai
→ uski poori row + column ko 0 karna hai
```

---

## ❗ Core Challenge

```text
Direct 0 karoge → naye 0 create honge → galat result ❌
```

👉 Isliye:

```text
“Decision aur modification alag-alag phase me karo”
```

---

# 🔍 Problem Classification

👉 Signals:

* Matrix traversal
* In-place modification
* Row + Column dependency

👉 Pattern:

```text
Simulation + Marking + Space Optimization
```

---

# ⚙️ Approach 1: Brute Force (Marker)

---

## 🧠 Idea

```text
0 milte hi direct change nahi karte
→ temporary marker use karte hain
→ end me marker → 0 convert
```

---

## 🧠 Real-Life Analogy

```text
Infected log milte hi turant isolate nahi karte
→ pehle unko tag lagate hain
→ end me sab tagged log isolate karte hain
```

---

## ⚠️ Key Issue

```text
Marker safe hona chahiye (float('inf') ✅)
-1 unsafe ❌
```

---

## ⏱️ Complexity

```text
Time → O(n*m*(n+m)) ❌
Space → O(1)
```

---

## ❌ Limitation

```text
Same row/column baar-baar process hoti hai
→ inefficient
```

---

# ⚙️ Approach 2: Better (Row + Column Arrays)

---

## 🧠 Idea

```text
Pehle decide karo kaunsi rows aur columns zero honi hain
→ fir ek baar me apply karo
```

---

## 🧠 Real-Life Analogy (VERY STRONG ⭐)

```text
Office me infection mila

❌ Turant sabko isolate nahi karte
✅ Pehle list banaate hain:
   kaunsi teams (rows) affected
   kaunse departments (columns) affected

→ fir ek baar me sabko isolate kar dete hain
```

---

## 🧠 Behind the Scenes (IMPORTANT ⭐)

👉 Step 1:

```text
row[i] = 1 → matlab poori row i zero hogi
col[j] = 1 → matlab poora column j zero hoga
```

👉 Step 2:

```text
Har cell check:
if row[i] == 1 OR col[j] == 1
→ usko 0 kar do
```

---

## 🔥 Dry Run

```text
1 1 1
1 0 1
1 1 1
```

👉 Step 1:

```text
row = [0,1,0]
col = [0,1,0]
```

👉 Step 2:

```text
1 0 1
0 0 0
1 0 1
```

---

## ⏱️ Complexity

```text
Time → O(n*m) ✅
Space → O(n + m) ❌
```

---

## 🧠 Memory Trick

```text
“Pehle decide → fir apply”
```

---

# 🚀 Approach 3: Optimal (Matrix Reuse)

---

## 🧠 Idea

```text
Extra arrays use nahi karenge
→ matrix ke first row aur first column ko marker bana denge
```

---

## 🧠 Real-Life Analogy (MASTER LEVEL ⭐)

```text
Tum office me ho

Better me:
→ alag diary me naam likh rahe the

Optimal me:
→ office ke entrance board par hi naam likh rahe ho 😏
```

👉 Matlab:

```text
First column → row markers
First row → column markers
```

---

## 🧠 Behind the Scenes (VERY IMPORTANT ⭐)

---

### 🔹 Step 1: Marking

👉 Jab 0 mile:

```text
matrix[i][0] = 0 → row i zero hogi
matrix[0][j] = 0 → column j zero hoga
```

---

### 🔹 Step 2: Apply

👉 Inner matrix:

```text
if matrix[i][0] == 0 OR matrix[0][j] == 0
→ cell = 0
```

---

### 🔹 Step 3: First Row & Column Fix

👉 Special handling:

```text
matrix[0][0] → first row ke liye
col0 → first column ke liye
```

---

## 🔥 Dry Run

```text
1 1 1
1 0 1
1 1 1
```

👉 Marking:

```text
1 0 1
0 0 1
1 1 1
```

👉 Apply:

```text
1 0 1
0 0 0
1 0 1
```

---

## ⏱️ Complexity

```text
Time → O(n*m) ✅
Space → O(1) 🔥
```

---

## ⚠️ Important Detail

```text
matrix[0][0] dono ka marker hai
→ conflict avoid karne ke liye col0 use hota hai
```

---

## 🧠 Memory Trick

```text
“Matrix ko hi marker bana do”
```

---

# 🎯 Comparison Table

| Approach | Time      | Space | Idea            |
| -------- | --------- | ----- | --------------- |
| Brute    | n*m*(n+m) | 1     | mark + convert  |
| Better   | n*m       | n+m   | external arrays |
| Optimal  | n*m       | 1     | matrix reuse    |

---

# 🚩 Interview Signals

👉 Agar bole:

* “in-place”
* “optimize space”
* “no extra array”

👉 Direct:

```text
Matrix reuse approach 🔥
```

---

# 📘 Revision Points

* Direct modify mat karo
* Marking → Applying separate rakho
* Row vs Column confusion avoid karo
* Optimal = reuse memory

---

# 🧠 FINAL SUMMARY

```text
Brute → mark everywhere (slow)
Better → store decisions (extra space)
Optimal → reuse matrix (smart 🔥)
```

---

# 💬 My Opinion

👉 Yeh problem:

```text
“DSA ka turning point hai”
```

👉 Agar tum isko samajh gaye:

* matrix problems easy ho jayenge
* space optimization clear ho jayega

---