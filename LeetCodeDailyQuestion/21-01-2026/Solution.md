class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num % 2 == 0:
                res.append(-1)
                continue

            cnt = 0
            temp = num
            while temp & 1:
                cnt += 1
                temp >>= 1

            res.append(num ^ (1 << (cnt - 1)))

        return res
