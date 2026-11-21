# 10 — Pipes and Cisterns

## Key Formulas & Shortcuts

| Concept | Formula |
|---|---|
| Filling pipe that fills the tank in **a** hours | Rate = **+1/a** of the tank per hour |
| Emptying pipe (leak) that empties it in **b** hours | Rate = **−1/b** of the tank per hour |
| Two filling pipes together | **ab / (a + b)** hours |
| One fills (a), one empties (b), with b > a | Net fill time = **ab / (b − a)** hours |

> **LCM trick (same as Time and Work):** Take tank capacity = LCM of all the times. Filling pipes then add whole units per hour and leaks subtract them.

---

## Question 1

Pipe A fills a tank in **12 hours** and pipe B fills it in **15 hours**. How long do they take together?

### Solution (LCM method)

1. Capacity = LCM(12, 15) = **60 units**
2. A = 5 units/hour and B = 4 units/hour, so together they fill **9 units/hour**
3. Time = 60 / 9 = **6⅔ hours** (6 hours 40 minutes)

### ✅ Answer: **6 hours 40 minutes**

---

## Question 2

A pipe fills a tank in **6 hours**. Because of a leak, it takes **8 hours**. How long would the leak alone take to empty a full tank?

### Solution

1. Capacity = LCM(6, 8) = **24 units**
2. The pipe fills 4 units/hour. With the leak, the net rate is 3 units/hour.
3. So the leak drains 4 − 3 = **1 unit/hour**
4. The leak empties 24 units in **24 hours**

**Shortcut:** ab / (b − a) = 6 × 8 / (8 − 6) = 24 ✔

### ✅ Answer: **24 hours**

---

## Question 3

Pipes A and B fill a tank in **20** and **30 minutes** respectively. Pipe C empties it in **15 minutes**. All three are opened together. When will the tank be full?

### Solution

1. Capacity = LCM(20, 30, 15) = **60 units**
2. A = +3, B = +2, C = −4 units/min, so the net rate is **+1 unit/min**
3. Time = 60 / 1 = **60 minutes**

### ✅ Answer: **1 hour**

---

## Takeaways

- Treat filling pipes as **positive** work and leaks as **negative** work. Everything else is the same as Time and Work.
- The LCM method avoids fraction arithmetic entirely.
- If the net rate is negative, the tank never fills. It empties instead.
