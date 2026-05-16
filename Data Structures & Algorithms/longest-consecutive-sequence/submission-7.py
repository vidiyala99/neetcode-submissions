class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0
        for i in nums:
            if(i-1 not in s):
                curr_num=i
                curr_size=1
                while(curr_num+1 in s):
                    curr_num+=1
                    curr_size+=1
                res=max(res,curr_size)
        return res
        