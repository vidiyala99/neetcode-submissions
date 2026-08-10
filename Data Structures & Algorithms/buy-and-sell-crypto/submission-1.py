class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_so_far=prices[0]
        for i in prices:
            if(i<min_so_far):
                min_so_far=i
            if(i-min_so_far>=0):
                max_profit=max(max_profit,i-min_so_far)
        return(max_profit)

        