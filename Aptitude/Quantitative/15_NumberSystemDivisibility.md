# 15 — Number System: Divisibility and Remainders

## Divisibility Rules

| Divisor | Rule |
|---|---|
| 2 | The last digit is even |
| 3 | The sum of the digits is divisible by 3 |
| 4 | The **last two** digits form a number divisible by 4 |
| 5 | The last digit is 0 or 5 |
| 6 | Divisible by both 2 **and** 3 |
| 8 | The **last three** digits form a number divisible by 8 |
| 9 | The sum of the digits is divisible by 9 |
| 11 | (Sum of digits in odd places) − (sum in even places) is 0 or a multiple of 11 |

## Remainder Shortcuts

| Concept | Rule |
|---|---|
| Remainder of a product | Multiply the remainders, then take the remainder again |
| Unit digit of powers | Unit digits repeat in cycles of up to **4** (for example 2 → 2, 4, 8, 6) |
| Number of factors of N = pᵃ × qᵇ × rᶜ | **(a+1)(b+1)(c+1)** |

---

## Question 1

Is **7,48,352** divisible by **8** and by **11**?

### Solution

1. **8:** the last three digits are 352, and 352 / 8 = 44. **Yes**
2. **11:** the digits are 7 4 8 3 5 2
   - Odd places from the right (2, 3, 4) add up to 9
   - Even places from the right (5, 8, 7) add up to 20
   - Difference = 11, which is a multiple of 11. **Yes**

### ✅ Answer: **Divisible by both 8 and 11**

---

## Question 2

Find the **unit digit** of **7⁹⁵**.

### Solution

1. Unit digits of powers of 7 repeat: 7, 9, 3, 1, a cycle of **4**
2. 95 mod 4 = **3**, so take the 3rd value in the cycle
3. The unit digit is **3**

### ✅ Answer: **3**

---

## Question 3

How many factors does **360** have?

### Solution

1. 360 = 2³ × 3² × 5¹
2. Number of factors = (3+1)(2+1)(1+1) = 4 × 3 × 2 = **24**

### ✅ Answer: **24**

---

## Takeaways

- For composite divisors such as 6, 12 or 15, check each **co-prime** factor separately.
- For a unit digit, find the cycle length, then use the **exponent mod cycle length**. If that gives 0, use the last value in the cycle.
- Counting factors only needs the **prime factorisation**.
