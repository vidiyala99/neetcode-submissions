class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        left,right=0,len(heights)-1
        while(left<right):
            length=right-left
            height=min(heights[left],heights[right])
            water_collected=length*height
            res=max(res,water_collected)
            if(heights[left]<heights[right]):
                left+=1
            else:
                right-=1
        return(res)
        