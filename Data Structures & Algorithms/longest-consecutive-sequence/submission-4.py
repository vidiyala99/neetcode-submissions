class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st=set(nums)
        res=0
        for i in nums:
            if(i-1 not in nums):
                current_num=i
                current_len=1
                while(current_num+1 in st):
                    current_num+=1
                    current_len+=1
                res=max(res,current_len)
        return res
        