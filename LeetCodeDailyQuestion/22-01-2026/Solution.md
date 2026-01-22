class Solution:



    def minimumPairRemoval(self, nums: List[int]) -> int:
        def checkSorted(nums):
            return sorted(nums)==nums
        def checkIndex(nums):
            minIndex=-1
            minSum=float('inf')
            for i in range(0,len(nums)-1,1):
                currSum=nums[i]+nums[i+1]
                if currSum<minSum:
                    minIndex=i
                    minSum=currSum
            return minIndex

        count=0
        flag=checkSorted(nums)
        while not flag:
            index=checkIndex(nums)
            nums[index]=nums[index]+nums[index+1]
            nums.pop(index+1)
            count+=1
            flag=checkSorted(nums)
        return count


        

        