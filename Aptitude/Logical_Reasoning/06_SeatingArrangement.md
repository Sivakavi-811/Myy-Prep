# 06 — Seating Arrangement

## Approach & Shortcuts

| Step | What to do |
|---|---|
| 1 | Draw the layout first: a row of slots, or a circle |
| 2 | Place the **definite** clues first, such as "A sits at an end" or "B is third from the left" |
| 3 | Then apply the **relative** clues, such as "C is to the immediate right of D" |
| 4 | When a clue allows two positions, try both. Drop the one that breaks a later clue |

### Direction conventions

| Layout | Left / Right |
|---|---|
| Linear row, facing **North** | Left and right are the same as yours |
| Linear row, facing **South** | Left and right are swapped |
| Circle, everyone facing the **centre** | Right = **anticlockwise**, Left = **clockwise** |

> **Tip:** In a circular arrangement there is no "first seat". Fix one person's position, then place everyone else relative to them.

---

## Question 1

Five friends P, Q, R, S and T sit in a row facing North.
- R is in the **middle**.
- P is at the **extreme left**.
- T is **immediately right of R**.
- Q is **not** next to P.

Who sits **second from the left**?

### Solution

1. There are 5 seats. P takes seat 1 and R takes seat 3
2. T is immediately right of R, so T takes seat 4
3. Seats 2 and 5 are left for Q and S. Q can't be next to P, so Q takes seat 5 and S takes seat 2
4. Order: **P S R T Q**

### ✅ Answer: **S**

---

## Question 2

Six people A, B, C, D, E and F sit around a circular table facing the centre.
- A sits **opposite** D.
- B is **immediately to the right** of A.
- C is **opposite** B.
- E is **not** next to A.

Who sits **between A and C**?

### Solution

1. Number the seats 1 to 6 going clockwise. Put A in seat 1, so D is in seat 4 (opposite)
2. Facing the centre, right means anticlockwise. B is immediately right of A, so B is in seat 6
3. C is opposite B, so C is in seat 3
4. Seats 2 and 5 are left for E and F. E can't be next to A (seat 2 is next to seat 1), so **E is in seat 5** and **F is in seat 2**
5. Going clockwise from A: A(1) → **F(2)** → C(3)

### ✅ Answer: **F**

---

## Takeaways

- Always place the **fixed** positions first, then use relative clues to fill in the rest.
- In a circle with everyone facing the centre, **right is anticlockwise**.
- Check the final arrangement against every clue before you answer.
