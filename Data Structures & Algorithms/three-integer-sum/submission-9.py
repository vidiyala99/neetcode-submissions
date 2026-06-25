class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        d = set()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = nums[left] + nums[right]
                triplet = (nums[i], nums[left], nums[right])
                if target + nums[i] == 0 and triplet not in d:  # fix: include nums[i] in sum check
                    d.add(triplet)        # tuples are hashable ✓
                    res.append(list(triplet))
                    left += 1             # move both pointers after a match
                    right -= 1
                elif target + nums[i] < 0:
                    left += 1
                else:
                    right -= 1

        return res
        