class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1,d2={},{}
        for i in range(len(nums)):
            d1[target-nums[i]]=i
        for i in range(len(nums)):
            k=target-nums[i]
            if(nums[i] in d1 and d1[nums[i]]!=i):
                return[i,d1[nums[i]]]