# Array

Quick-scan index of every Array problem solved. No code here — just enough to
jog your memory on the pattern before you open the actual solution file.

| #  | Problem                             | Pattern                                | Difficulty | Time   | Space      | Link                                                                                   | Solution                                                                           | Mental Model                                      | Status |
| -- | ----------------------------------- | -------------------------------------- | ---------- | ------ | ---------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------- | ------ |
| 1  | Two Sum                             | Hashmap                                | Easy       | O(n)   | O(n)       | [LC](https://leetcode.com/problems/two-sum/)                                           | [01-two-sum.py](solutions/01-two-sum.py)                                           | [Notes](notes/01-two-sum.md)                      | ⬜      |
| 2  | Best Time to Buy and Sell Stock     | Two-pointer / min-max tracking         | Easy       | O(n)   | O(1)       | [LC](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)                   | [02-best-time-to-buy-sell-stock.py](solutions/02-best-time-to-buy-sell-stock.py)   | [Notes](notes/02-best-time-to-buy-sell-stock.md)  | ⬜      |
| 3  | Two Sum II (sorted input)           | Two-pointer                            | Easy       | O(n)   | O(1)       | [LC](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)                  | [03-two-sum-ii.py](solutions/03-two-sum-ii.py)                                     | [Notes](notes/03-two-sum-ii.md)                   | ⬜      |
| 4  | Contains Duplicate                  | Hashmap                                | Easy       | O(n)   | O(n)       | [LC](https://leetcode.com/problems/contains-duplicate/)                                | [04-contains-duplicate.py](solutions/04-contains-duplicate.py)                     | [Notes](notes/04-contains-duplicate.md)           | ⬜      |
| 5  | Maximum Subarray                    | Kadane's Algorithm                     | Easy       | O(n)   | O(1)       | [LC](https://leetcode.com/problems/maximum-subarray/)                                  | [05-maximum-subarray.py](solutions/05-maximum-subarray.py)                         | [Notes](notes/05-maximum-subarray.md)             | ⬜      |
| 6  | 3Sum                                | Two-pointer (sorted + fix one element) | Medium     | O(n²)  | O(1)–O(n)  | [LC](https://leetcode.com/problems/3sum/)                                              | [06-3sum.py](solutions/06-3sum.py)                                                 | [Notes](notes/06-3sum.md)                         | ⬜      |
| 7  | Product of Array Except Self        | Prefix/Suffix product (logical)        | Medium     | O(n)   | O(1) extra | [LC](https://leetcode.com/problems/product-of-array-except-self/)                      | [07-product-except-self.py](solutions/07-product-except-self.py)                   | [Notes](notes/07-product-except-self.md)          | ⬜      |
| 8  | Container With Most Water           | Two-pointer                            | Medium     | O(n)   | O(1)       | [LC](https://leetcode.com/problems/container-with-most-water/)                         | [08-container-with-most-water.py](solutions/08-container-with-most-water.py)       | [Notes](notes/08-container-with-most-water.md)    | ⬜      |
| 9  | Subarray Sum Equals K               | Running sum + Hashmap                  | Medium     | O(n)   | O(n)       | [LC](https://leetcode.com/problems/subarray-sum-equals-k/)                             | [09-subarray-sum-equals-k.py](solutions/09-subarray-sum-equals-k.py)               | [Notes](notes/09-subarray-sum-equals-k.md)        | ⬜      |
| 10 | Longest Subarray with Sum K         | Running sum + Hashmap                  | Medium     | O(n)   | O(n)       | [GfG](https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1/) | [10-longest-subarray-sum-k.py](solutions/10-longest-subarray-sum-k.py)             | [Notes](notes/10-longest-subarray-sum-k.md)       | ⬜      |
| 11 | Minimum Size Subarray Sum           | Sliding window (running sum + pointer) | Medium     | O(n)   | O(1)       | [LC](https://leetcode.com/problems/minimum-size-subarray-sum/)                         | [11-min-size-subarray-sum.py](solutions/11-min-size-subarray-sum.py)               | [Notes](notes/11-min-size-subarray-sum.md)        | ⬜      |
| 12 | K-diff Pairs in an Array            | Hashmap                                | Medium     | O(n)   | O(n)       | [LC](https://leetcode.com/problems/k-diff-pairs-in-an-array/)                          | [12-k-diff-pairs.py](solutions/12-k-diff-pairs.py)                                 | [Notes](notes/12-k-diff-pairs.md)                 | ⬜      |
| 13 | Maximum Length of Repeated Subarray | DP (2D) / sliding comparison           | Medium     | O(n·m) | O(n·m)     | [LC](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)               | [13-max-length-repeated-subarray.py](solutions/13-max-length-repeated-subarray.py) | [Notes](notes/13-max-length-repeated-subarray.md) | ⬜      |

---

## Pattern Cheat-Sheet (Array)

### Hashmap

* Seen-before lookups
* Complement search (Two Sum)
* Frequency counting
* Fast existence checks

### Two-Pointer

* Sorted arrays
* Pair/triplet problems
* Shrinking search space from both ends

### Kadane's Algorithm

* Maximum/minimum contiguous subarray
* Running best vs current best
* Reset when current contribution becomes harmful

### Running Sum + Hashmap

* Subarray Sum = K
* Prefix sum storage
* Count previous occurrences

### Sliding Window

* Contiguous subarray problems
* Grow window until condition met
* Shrink while maintaining validity

### Prefix/Suffix

* Need left and right information simultaneously
* Avoid division
* Precompute directional information

### Dynamic Programming

* Overlapping subproblems
* Store previous computations
* Build solution incrementally

---

## Mental Model Template

Create one file per problem inside the `notes/` folder.

Example: `notes/01-two-sum.md`

### Template

```md
# Problem Name

## Pattern
Hashmap

## Brute Force Thought
What is the obvious solution and why is it too slow?

## Key Observation
What insight unlocks the optimal solution?

## Mental Model
Explain the problem in simple words.

## Pattern Trigger
What clues in the question tell me to use this pattern?

## Algorithm Flow
1.
2.
3.

## Common Mistakes
-
-

## Complexity
Time:
Space:

## 30-Second Revision
One-line takeaway that helps you recall the solution instantly.
```

---

### Status Legend

* ⬜ Not Started
* 🟨 In Progress
* ✅ Solved & Reviewed
* 🧠 Mental Model Completed
