# 05 — Syllogisms

## Approach & Shortcuts

Solve syllogisms with **Venn diagrams**. Draw the **minimum overlap** the statements allow. A conclusion follows only if it is true in **every** possible diagram.

| Statement | Meaning |
|---|---|
| **All A are B** | Circle A sits completely inside circle B |
| **Some A are B** | A and B overlap at least partly |
| **No A is B** | A and B don't touch |
| **Some A are not B** | Part of A lies outside B |

### Quick rules

| Premises | Definite conclusion |
|---|---|
| All + All | **All** (All A are B, All B are C → All A are C) |
| All + No | **No** (All A are B, No B is C → No A is C) |
| Some + All | **Some** (Some A are B, All B are C → Some A are C) |
| Some + Some | **No definite conclusion** |
| All A are B | Converse: **Some B are A** is true. **All B are A** is not certain |

> **"Either-or" case:** If neither "Some A are C" nor "No A is C" can be proved, but those two statements together cover every possibility, the answer is **"Either I or II follows"**.

---

## Question 1

**Statements:** All dogs are animals. All animals are living beings.
**Conclusions:** I. All dogs are living beings. II. Some living beings are dogs.

### Solution

1. Dogs ⊂ Animals ⊂ Living beings, so **I follows** (All + All = All)
2. All dogs are living beings, so some living beings must be dogs. **II follows** by conversion

### ✅ Answer: **Both I and II follow**

---

## Question 2

**Statements:** Some pens are books. All books are tables.
**Conclusions:** I. Some pens are tables. II. All tables are pens.

### Solution

1. The pens that are books are also tables, so **I follows** (Some + All = Some)
2. Tables could include many things that aren't pens, so **II does not follow**

### ✅ Answer: **Only I follows**

---

## Question 3

**Statements:** Some cats are rats. Some rats are bats.
**Conclusions:** I. Some cats are bats. II. No cat is a bat.

### Solution

1. Some + Some gives **no definite conclusion**. Cats and bats might overlap or might not
2. Neither conclusion can be proved on its own
3. But one of them must be true: either some cats are bats, or none are

### ✅ Answer: **Either I or II follows**

---

## Takeaways

- Draw the **least-overlap** diagram, then try to break each conclusion with a different valid diagram.
- "Some" means **at least one**, possibly all.
- Look for the either-or pair: a "Some" statement and a "No" statement about the same two groups.
