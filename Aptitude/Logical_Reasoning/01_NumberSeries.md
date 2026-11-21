# 01 — Number Series

## Common Patterns to Check (in this order)

| Pattern | How to spot it | Example |
|---|---|---|
| Constant difference | Differences are equal | 3, 7, 11, 15 (+4) |
| Difference of differences | 2nd-level differences are equal | 2, 5, 10, 17 (+3, +5, +7) |
| Multiplication / ratio | Each term ≈ previous × k | 3, 6, 12, 24 (×2) |
| Mixed (× then +) | Terms grow faster than additions alone | 1, 3, 7, 15 (×2 + 1) |
| Squares / cubes | Terms close to n² or n³ | 1, 4, 9, 16 / 2, 9, 28, 65 (n³ + 1) |
| Alternating series | Odd and even positions follow separate rules | 2, 10, 4, 20, 6, 30 |

> **Shortcut:** Write the first differences under the series. If they don't settle the pattern, check the ratios between terms. If neither works, try squares and cubes.

---

## Question 1

Find the next term: **2, 6, 12, 20, 30, ?**

### Solution

1. Differences: 4, 6, 8, 10. They rise by 2 each time.
2. Next difference = **12**
3. Next term = 30 + 12 = **42**

**Alternate view:** the terms are n(n + 1): 1×2, 2×3, 3×4, 4×5, 5×6, so the next is 6×7 = 42 ✔

### ✅ Answer: **42**

---

## Question 2

Find the next term: **3, 7, 15, 31, 63, ?**

### Solution

1. Ratios are close to 2, so try **× 2 + 1**:
   3×2+1 = 7, 7×2+1 = 15, 15×2+1 = 31, 31×2+1 = 63 ✔
2. Next term = 63 × 2 + 1 = **127**

### ✅ Answer: **127**

---

## Question 3

Find the wrong term: **1, 8, 27, 64, 124, 216**

### Solution

1. The terms look like cubes: 1³, 2³, 3³, 4³, ?, 6³
2. 5³ = **125**, but the series has 124

### ✅ Answer: **124** (should be 125)

---

## Takeaways

- Start with differences, then ratios, then squares and cubes.
- If the series jumps up and down, split it into odd-position and even-position terms.
- Check your pattern against **every** term, not only the first two.
