# 04 — Direction Sense

## Approach & Shortcuts

```
            N
       NW   |   NE
   W -------+------- E
       SW   |   SE
            S
```

| Rule | Detail |
|---|---|
| Turning right | N → E → S → W → N (clockwise) |
| Turning left | N → W → S → E → N (anticlockwise) |
| Shortest distance | **Pythagoras**: √(x² + y²) |
| Shadows | Sunrise (morning): the shadow falls **West**. Sunset (evening): the shadow falls **East** |

> **Coordinate method:** Start at (0, 0). North is +y and East is +x. Add up each move, then read off the final position and distance.

---

## Question 1

Ravi walks **10 m North**, turns right and walks **6 m**, then turns right again and walks **2 m**. How far is he from the start, and in which direction?

### Solution (coordinates)

1. 10 m North takes him to (0, 10)
2. Turning right means facing East. 6 m takes him to (6, 10)
3. Turning right again means facing South. 2 m takes him to (6, 8)
4. Distance = √(6² + 8²) = √100 = **10 m**
5. The final point is up and to the right of the start, so he is **North-East** of it

### ✅ Answer: **10 m, North-East**

---

## Question 2

A man faces **South**. He turns **90° clockwise**, then **180° anticlockwise**. Which direction does he face now?

### Solution

1. Starting from South, 90° clockwise takes him to **West**
2. From West, 180° anticlockwise takes him to **East**

### ✅ Answer: **East**

---

## Question 3

One morning after sunrise, Meena stands facing a pole. The pole's shadow falls exactly to her **right**. Which direction is she facing?

### Solution

1. In the morning the sun is in the East, so shadows fall to the **West**
2. The shadow is on her right, so her right side points West
3. If your right hand points West, you are facing **South**

### ✅ Answer: **South**

---

## Takeaways

- Use coordinates for walking problems. They remove any confusion about turns.
- A clockwise turn is a right turn, and an anticlockwise turn is a left turn.
- The shortest distance is the straight line between start and end, worked out with Pythagoras.
