class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0
        for i in nums:
            if(i-1 not in nums):
                x=i
                size=1
                while(x+1 in s):
                    x+=1
                    size+=1
                res=max(res,size)
        return res
        