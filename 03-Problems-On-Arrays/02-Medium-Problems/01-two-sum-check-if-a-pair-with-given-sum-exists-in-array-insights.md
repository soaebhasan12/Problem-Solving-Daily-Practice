# 📄 01 - Two Sum (Check if Pair Exists in Array) Insights


## 🧠 Problem Understanding

Given an array `nums` and a target `k`, check:

👉 **kya koi 2 elements exist karte hain jinka sum = k ho?**

👉 Return:

* indices (Two Sum type)
* ya boolean (pair exists?)

---

## 🔍 Key Insight

```
Instead of checking all pairs,
we convert problem into lookup problem using hashmap
```

👉 Question ban jata hai:

👉 **“kya required number pehle kabhi aaya hai?”**

---

# ⚙️ Approach 1: Brute Force (Nested Loop)

## 💡 Idea

* Har element ke liye
* baaki sab elements check karo

---

## 🧪 Code

```python
def two_sum_bruteforce(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return [-1, -1]
```

---

## ⏱️ Time Complexity

```
O(n²)
```

---

## 🚫 Problems

* Slow for large inputs
* Same work repeat hota hai
* Interview me reject ❌

---

# ⚡ Approach 2: Optimal (HashMap)

## 💡 Core Idea

```
For every element:
required = target - nums[i]

Check:
required pehle dekha hai ya nahi?
```

---

## 🧠 Logic Breakdown

### Step 1: Loop

```
for i in range(len(nums))
```

---

### Step 2: Required nikaalo

```
required = target - nums[i]
```

---

### Step 3: Check in map

```
if required in map:
```

👉 matlab pair mil gaya ✅

---

### Step 4: Return indices

```
return [map[required], i]
```

---

### Step 5: Store current element

```
map[nums[i]] = i
```

---

## 🧪 Complete Code

```python
def two_sum(nums, target):
    map_dict = {}
    
    for i in range(len(nums)):
        required = target - nums[i]
        
        if required in map_dict:
            return [map_dict[required], i]
        
        map_dict[nums[i]] = i
    
    return [-1, -1]
```

---

## ⏱️ Time Complexity

```
O(n)
```

---

## 📦 Space Complexity

```
O(n)
```

---

# 🔥 Dry Run Insight

Example:

```
nums = [2, 7, 11, 15]
target = 9
```

Flow:

```
Step 1: 2 → store
Step 2: 7 → required = 2 → found ✅
```

👉 Answer:

```
[0, 1]
```

---

# ⚠️ Your Mistakes (VERY IMPORTANT 🚨)

## ❌ Mistake 1: Wrong return

```python
return [i, map_dict[i]]
```

👉 Problem:

* tu current index use kar raha tha ❌
* required ka index lena tha ✅

✔️ Correct:

```python
return [map_dict[required], i]
```

---

## ❌ Mistake 2: Logic confusion

👉 Tu soch raha tha:

```
map_dict[i]
```

👉 But map me kya store hai?

```
value → index
```

👉 So access hoga:

```
map_dict[value]
```

---

## ❌ Mistake 3: Pattern miss kar raha tha

👉 Problem ka real pattern tha:

```
"check previous element existence"
```

👉 Yeh direct hashing signal hai 🚩

---

# 🧠 Important Observations

* HashMap → O(1) lookup deta hai
* Value → index store hota hai
* Ek pass me solution mil jata hai

---

# 🧠 Memory Trick

```
target - current → check map
```

---

# 🎯 Final Insight

```
Brute force → try all pairs
Optimal → convert into lookup problem
```

---

# 🧠 Summary

* Pair find karna → hashing use karo
* required = target - current
* map me check karo
* milte hi return

---

# 🚀 Interview Point

👉 “We reduce time complexity from O(n²) to O(n) using hashmap lookup”

---

## 🔥 Quick Check:

Agar:

```
nums = [3, 2, 4]
target = 6
```

👉 Jab tu `4` pe hoga:

👉 required kya hoga?

👉 Sirf number bata 😏
