# 1292. Maximum Side Length of a Square with Sum ≤ Threshold

**Difficulty:** Medium  
**Topic:** Prefix Sum, Binary Search, Matrix  

---

## Problem Statement

Given an `m x n` matrix `mat` and an integer `threshold`, return the **maximum side length** of a square submatrix such that the **sum of its elements is less than or equal to `threshold`**.

If no such square exists, return `0`.

---

## Examples

### Example 1

**Input**
```

mat = [
[1, 1, 3, 2, 4, 3, 2],
[1, 1, 3, 2, 4, 3, 2],
[1, 1, 3, 2, 4, 3, 2]
]
threshold = 4

```

**Output**
```

2

```

**Explanation**  
The largest square with sum ≤ 4 has side length `2`.

---

### Example 2

**Input**
```

mat = [
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2],
[2, 2, 2, 2, 2]
]
threshold = 1

```

**Output**
```

0

```

**Explanation**  
No square submatrix satisfies the condition.

---

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 ≤ m, n ≤ 300`
- `0 ≤ mat[i][j] ≤ 10⁴`
- `0 ≤ threshold ≤ 10⁵`

---

## Notes

- Prefix sums help compute submatrix sums efficiently.
- Binary search can be used to optimize checking possible square sizes.
```

If you want, I can also:

* Add a **solution section**
* Include **time & space complexity**
* Format it for a **LeetCode solutions repository**

Just tell me 👍
