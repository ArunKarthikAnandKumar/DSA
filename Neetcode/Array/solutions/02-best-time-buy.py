"""
Problem  : Two Sum
Link     : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Pattern  : Sliding Window
Time     : O(n)
Space    : O(n)

Brute Force Thought:
We can just run 2 for loops to check but it takes O(n^2) time

Key Observation
if x+y=n search for n-y in the Target

The complement Element Should always be Target-nums[i] not the other way around
Trigger  : "find pair that sums to target" + need O(n) -> store complements
Logic: to find the pair need to maintain HashMap which looks for complement in HM, but adds the Normal Element Only

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=r=0
        res=0
        while r <len(prices):
            if prices[r]>prices[l]:
                res=max(res,prices[r]-prices[l])
            if prices[l]>prices[r]:
                l=r
            r+=1
        return res
        