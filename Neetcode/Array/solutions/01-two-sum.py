"""
Problem  : Two Sum
Link     : https://leetcode.com/problems/two-sum/
Pattern  : Hashmap

Brute Force Thought:
We can just run 2 for loops to check but it takes O(n^2) time

Key Observation
if x+y=n search for n-y in the Target

The complement Element Should always be Target-nums[i] not the other way around
Trigger  : "find pair that sums to target" + need O(n) -> store complements
Logic: to find the pair need to maintain HashMap which looks for complement in HM, but adds the Normal Element Only
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
