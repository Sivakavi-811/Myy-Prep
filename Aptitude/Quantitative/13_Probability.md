# 13 — Probability

## Key Formulas & Shortcuts

| Concept | Formula |
|---|---|
| Probability of an event | **P(E) = favourable outcomes / total outcomes** |
| Complement | **P(not E) = 1 − P(E)** |
| A or B (addition rule) | **P(A ∪ B) = P(A) + P(B) − P(A ∩ B)** |
| A and B, independent events | **P(A ∩ B) = P(A) × P(B)** |
| Dice | One die has 6 outcomes. Two dice have **36** outcomes |
| Cards | 52 cards: 4 suits of 13. There are 26 red, 26 black, 12 face cards, and 4 aces |

> **"At least one" trick:** P(at least one) = 1 − P(none). This is almost always quicker than adding up every case.

---

## Question 1

Two dice are thrown. What is the probability that the sum is **8**?

### Solution

1. Total outcomes = 6 × 6 = **36**
2. Pairs that give 8: (2,6), (3,5), (4,4), (5,3), (6,2), which is **5** outcomes
3. P = **5/36**

### ✅ Answer: **5/36**

---

## Question 2

A bag holds **4 red** and **6 blue** balls. Two balls are drawn **without replacement**. What is the probability that **both are red**?

### Solution

1. Ways to choose 2 red balls = ⁴C₂ = **6**
2. Ways to choose any 2 balls = ¹⁰C₂ = **45**
3. P = 6/45 = **2/15**

**Sequential check:** 4/10 × 3/9 = 12/90 = 2/15 ✔

### ✅ Answer: **2/15**

---

## Question 3

A coin is tossed **3 times**. What is the probability of getting **at least one head**?

### Solution

1. P(no heads) = P(TTT) = (1/2)³ = **1/8**
2. P(at least one head) = 1 − 1/8 = **7/8**

### ✅ Answer: **7/8**

---

## Takeaways

- Count outcomes with combinations when order doesn't matter, as in Question 2.
- For "at least one", use the complement: 1 − P(none).
- "Without replacement" changes the totals after each draw. Multiply the probabilities in sequence or use combinations.
