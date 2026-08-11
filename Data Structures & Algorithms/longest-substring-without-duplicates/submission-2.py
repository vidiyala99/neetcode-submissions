class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        left=0
        res=0
        for i in range(len(s)):
            while(s[i] in d):
                d.remove(s[left])
                left+=1
            d.add(s[i])

            res=max(res,i-left+1)
        return res


        