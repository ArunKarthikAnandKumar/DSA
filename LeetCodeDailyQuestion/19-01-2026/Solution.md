# 1292. Maximum Side Length of a Square with Sum ≤ Threshold

## Intuition

To efficiently calculate the sum of every possible square submatrix, we need to **optimize repeated sum calculations**.

A brute-force approach would be too slow because:
- Matrix size can be up to `300 x 300`
- Checking every square repeatedly would lead to **O(n⁴)** complexity

To optimize this, we use **Prefix Sum**.

---

## Step 1: Prefix Sum Matrix

We build a prefix sum matrix `pref` where:

```

pref[i][j] = sum of all elements from (0,0) to (i,j)

```

### Formula

```

pref[i][j] = pref[i-1][j]
+ pref[i][j-1]
- pref[i-1][j-1]
+ mat[i][j]

```

This allows us to compute the sum of **any submatrix in O(1) time**.

---

## Step 2: Get Sum of a Square Submatrix

To compute the sum of a square from **top-left `(i, j)`**  
to **bottom-right `(r2, c2)`**, use:

```

sum = pref[r2][c2]
- pref[i-1][c2]
- pref[r2][j-1]
+ pref[i-1][j-1]

```

Boundary checks are required when `i == 0` or `j == 0`.

---

## Step 3: Iterate Over All Possible Squares

- For each cell `(i, j)` as the **top-left corner**
- Increase the square size (`offset`)
- Compute `(r2, c2)` using:

```

r2 = i + offset
c2 = j + offset

````

- If the sum ≤ `threshold`, update the answer
- Stop expanding once sum exceeds threshold or bounds are crossed

---

## Python Implementation

```python
class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Step 1: Build prefix sum matrix
        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (
                    pref[i - 1][j]
                    + pref[i][j - 1]
                    - pref[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        # Step 2 & 3: Try all square sizes
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                size = max_len + 1
                while i + size - 1 <= m and j + size - 1 <= n:
                    r2 = i + size - 1
                    c2 = j + size - 1

                    square_sum = (
                        pref[r2][c2]
                        - pref[i - 1][c2]
                        - pref[r2][j - 1]
                        + pref[i - 1][j - 1]
                    )

                    if square_sum <= threshold:
                        max_len = size
                        size += 1
                    else:
                        break

        return max_len
````

---

## Time Complexity

* Prefix sum construction: **O(m × n)**
* Square checking: **O(m × n × min(m, n))**
* Optimized due to early breaks

**Overall:** `O(m × n × min(m, n))`

---

## Space Complexity

* Prefix sum matrix: **O(m × n)**

---

## Key Takeaways

* Prefix sum reduces submatrix sum queries from **O(n²) → O(1)**
* Expanding squares greedily avoids unnecessary checks
* This approach efficiently handles large matrices

---

✅ Clean
✅ Efficient
✅ Interview-ready

If you want:

* **Binary search optimization**
* **Dry run explanation**
* **Java version**

Just tell me 👍
