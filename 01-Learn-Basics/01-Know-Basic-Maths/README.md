# 🧠 1️⃣ Prime Number – Core Concept (Never Forget)

### Definition

Prime = exactly 2 divisors
👉 1 and itself

### Composite

Composite = 2 se zyada divisors

---

# 🧠 2️⃣ Most Important Mathematical Insight

If n is composite
→ n = a × b

At least one of a or b ≤ √n

WHY?

Agar dono √n se bade hote
→ a × b > n
→ impossible

Isliye prime check me √n tak check karna enough hai.

---

# 🧠 3️⃣ Prime Checking Mental Model

Correct thinking:

1. If n <= 1 → not prime
2. Loop i from 2 to √n
3. If n % i == 0 → composite
4. If no divisor found → prime

Important:

Loop limit logic alag hota hai
Divisibility condition alag hoti hai

Tumne dono mix kiya tha.
Ye mistake yaad rakho.

---

# 🧠 4️⃣ Divisor Concept – Golden Rule

If i divides n
→ n // i also divides n

Divisors come in pairs.

Except perfect square case
where i == n//i

---

# 🧠 5️⃣ Perfect Square Insight

If divisor count is odd
→ number perfect square hai

Because only perfect square me ek pair collapse hota hai.

---

# 🧠 6️⃣ Optimization Pattern

Naive divisor check → O(n)
Optimized divisor check → O(√n)

Prime check → O(√n)

Whenever factor/divisor word dikhe
→ brain automatically √n sochna chahiye.

---

# 🧠 7️⃣ Common Coding Mistakes (Tumhari Personal Mistake List)

Ye specially tumhare liye:

✔ `%` check bhool jaana
✔ Loop limit galat rakhna
✔ `i*i <= n` ko divisor condition samajhna
✔ `.append()` ko assign kar dena
✔ `.sort()` ko return kar dena
✔ original number destroy kar dena
✔ inclusive boundary miss karna

Isko “Mistake Journal” me likho.

---

# 🧠 8️⃣ Edge Cases Always Check

For prime:

n <= 1 → not prime
2 → prime
even > 2 → not prime

For divisor problems:

n = 1
perfect square case
duplicate pair case

---

# 🧠 9️⃣ Pattern Recognition Skill

Digit extraction pattern
Divisor pair pattern
√n optimization pattern

Ye 3 patterns baar-baar repeat honge.

DSA me patterns yaad rakho, code nahi.

---

# 🧠 10️⃣ Long-Term Memory Strategy

Har topic ke liye 3 cheezein likho:

1. Core math idea
2. Optimization idea
3. Common mistakes

Agar ye 3 clear hain
to concept kabhi nahi bhoologe.

---