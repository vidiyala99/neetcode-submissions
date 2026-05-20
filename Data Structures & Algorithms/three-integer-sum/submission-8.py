from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        i = 0
        while i < len(nums) - 2:
            x = i + 1
            y = len(nums) - 1
            
            while x < y:
                s = nums[i] + nums[x] + nums[y]
                if s > 0:
                    y -= 1
                elif s < 0:
                    x += 1
                else:
                    res.append([nums[i], nums[x], nums[y]])
                    x += 1
                    # FIX 1: Put 'x < y' first to avoid IndexError
                    while x < y and nums[x] == nums[x - 1]:
                        x += 1
            
            # FIX 2: Skip duplicates for 'i' at the bottom of the loop
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
                
            i += 1  # Move to the next unique anchor element
            
        return res