
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod, right_prod, res = [1] * n, [1] * n, [1] * n

        # Prefix products
        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]

        # Suffix products
        for i in range(n - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]

        # Multiply prefix and suffix products
        for i in range(n):
            res[i] = left_prod[i] * right_prod[i]

        return res
