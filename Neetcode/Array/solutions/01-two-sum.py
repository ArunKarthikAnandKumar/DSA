"""
Problem  : Two Sum
Link     : https://leetcode.com/problems/two-sum/
Pattern  : Hashmap
Trigger  : "find pair that sums to target" + need O(n) -> store complements
Time     : O(n)
Space    : O(n)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
