we need to find number x such that x or x+1 is ==nums[i] return minimum x if x is not found return -1

for each num you only need to check till n-1

BruteForce

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        n=len(nums)
        for i in range(n):
            for j in range(nums[i]):
                if (j | j+1)==nums[i]:
                    res[i]=j
                    break
            
        return res

#Optimal Approach 
differnce between x and x+1
x+1 is x such that the first nonzero is flipped to 1 rest all before 0
x | x+1 we get first non zer flip and one before that 
to get x find first zero in nums[i] and flip the bit before that and return as it is

Minimum we get if we put 0 in MSB

TO CHECK IF A BIT is 1 or not (nums[i] & (1<<j))>0
to make prev bit 0 nums[i]^(1<<j-1)