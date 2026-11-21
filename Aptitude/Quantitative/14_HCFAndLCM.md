# 14 — HCF and LCM

## Key Formulas & Shortcuts

| Concept | Formula |
|---|---|
| Product rule (two numbers only) | **HCF × LCM = a × b** |
| HCF by prime factorisation | Multiply the **lowest** power of each **common** prime |
| LCM by prime factorisation | Multiply the **highest** power of **every** prime that appears |
| HCF of fractions | **HCF of numerators / LCM of denominators** |
| LCM of fractions | **LCM of numerators / HCF of denominators** |
| Euclid's method | **HCF(a, b) = HCF(b, a mod b)**, repeated until the remainder is 0 |

> **Remainder patterns:**
> - Largest number that divides x, y, z leaving the **same remainder** = HCF of the differences (y − x, z − y).
> - Smallest number that leaves remainder r when divided by a, b, c = **LCM(a, b, c) + r**.

---

## Question 1

Find the HCF and LCM of **36** and **84**.

### Solution

1. 36 = 2² × 3² and 84 = 2² × 3 × 7
2. HCF = 2² × 3 = **12**
3. LCM = 2² × 3² × 7 = **252**

**Check:** 12 × 252 = 3024 = 36 × 84 ✔

### ✅ Answer: **HCF = 12, LCM = 252**

---

## Question 2

Three bells ring at intervals of **6, 8 and 12 minutes**. They ring together at **9:00 AM**. When will they next ring together?

### Solution

1. They ring together again after LCM(6, 8, 12) minutes
2. 6 = 2 × 3, 8 = 2³, 12 = 2² × 3, so LCM = 2³ × 3 = **24 minutes**
3. 9:00 AM + 24 minutes = **9:24 AM**

### ✅ Answer: **9:24 AM**

---

## Question 3

Find the largest number that divides **43, 91 and 183** and leaves the **same remainder** each time.

### Solution

1. The answer is the HCF of the differences: 91 − 43 = 48, 183 − 91 = 92, 183 − 43 = 140
2. HCF(48, 92) = 4, and HCF(4, 140) = **4**

**Check:** 43, 91 and 183 each leave remainder 3 when divided by 4 ✔

### ✅ Answer: **4**

---

## Takeaways

- Questions about things happening "together again", bells, or meeting points use the **LCM**.
- Questions about the "largest size", "greatest number", or cutting into equal pieces use the **HCF**.
- HCF × LCM = product works **only for two numbers**.
