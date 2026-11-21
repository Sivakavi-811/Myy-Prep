# 12 — Permutations and Combinations

## Key Formulas & Shortcuts

| Concept | Formula | Use it when |
|---|---|---|
| Permutation | **ⁿPᵣ = n! / (n − r)!** | **Order matters** (arrangements, ranks, passwords) |
| Combination | **ⁿCᵣ = n! / (r! (n − r)!)** | **Order doesn't matter** (teams, committees, selections) |
| Arranging with repeated items | **n! / (p! q! …)** | Letters repeat, e.g. in "BANANA" |
| Circular arrangement | **(n − 1)!** | People seated around a round table |
| Symmetry | **ⁿCᵣ = ⁿCₙ₋ᵣ** | Makes large calculations shorter |

> **Key question:** If you swap two of the chosen items, do you get a different outcome? If **yes**, use a permutation. If **no**, use a combination.

---

## Question 1

In how many ways can **3 students** be chosen from **8** for a committee?

### Solution

1. A committee has no order, so this is a **combination**
2. ⁸C₃ = 8! / (3! × 5!) = (8 × 7 × 6) / (3 × 2 × 1) = **56**

### ✅ Answer: **56**

---

## Question 2

How many different arrangements can be made from the letters of **"BANANA"**?

### Solution

1. There are 6 letters in total: A appears 3 times, N twice, and B once
2. Arrangements = 6! / (3! × 2!) = 720 / 12 = **60**

### ✅ Answer: **60**

---

## Question 3

In how many ways can **5 boys and 3 girls** sit in a row so that **all the girls sit together**?

### Solution

1. Treat the 3 girls as **one block**. There are now 5 boys + 1 block = 6 units
2. The 6 units can be arranged in 6! = **720** ways
3. Inside the block, the girls can be arranged in 3! = **6** ways
4. Total = 720 × 6 = **4,320**

### ✅ Answer: **4,320**

---

## Takeaways

- Decide whether **order matters** before choosing a formula.
- **Together** constraint: treat the group as one unit, then multiply by the arrangements inside the group.
- **Not together**: total arrangements minus the arrangements where they are together.
- Repeated items: divide by the factorial of each repeat count.
