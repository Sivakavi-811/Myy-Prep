# 03 — Coding-Decoding

## Approach & Shortcuts

| Pattern type | What to check |
|---|---|
| Letter shift | Is each letter moved forward or back by a fixed amount (+1, −2, …)? |
| Reverse alphabet | A ↔ Z, B ↔ Y, …; the two letters' positions add up to **27** |
| Position value | Letters turned into numbers (A = 1 … Z = 26), sums, or products |
| Rearrangement | Letters of the word reversed or swapped in pairs |

> **Memorise the position landmarks "EJOTY":** E = 5, J = 10, O = 15, T = 20, Y = 25. They let you find any letter's position quickly.

---

## Question 1

If **CAT** is coded as **DBU**, how is **DOG** coded?

### Solution

1. C → D, A → B, T → U, so every letter moves **+1**
2. D → E, O → P, G → H

### ✅ Answer: **EPH**

---

## Question 2

If **APPLE** is coded as **ZKKOV**, how is **MANGO** coded?

### Solution

1. A(1) → Z(26), P(16) → K(11), L(12) → O(15), E(5) → V(22)
2. Each pair adds up to **27**, so this is the reverse-alphabet code
3. M(13) → N(14), A(1) → Z(26), N(14) → M(13), G(7) → T(20), O(15) → L(12)

### ✅ Answer: **NZMTL**

---

## Question 3

If **BAD** = **7** and **CAB** = **6**, what is **FACE**?

### Solution

1. BAD: B(2) + A(1) + D(4) = **7** ✔
2. CAB: C(3) + A(1) + B(2) = **6** ✔
3. So the code is the sum of letter positions. FACE = F(6) + A(1) + C(3) + E(5) = **15**

### ✅ Answer: **15**

---

## Takeaways

- Write the alphabet positions under both the word and its code. The pattern is usually clear right away.
- If the shift changes from letter to letter (+1, +2, +3 …), check for a growing or alternating pattern.
- Test the rule on **every** letter before using it.
