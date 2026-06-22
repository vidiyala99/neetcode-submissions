class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,s2={},{}
        for i in s:
            if(i not in s1):
                s1[i]=1
            else:
                s1[i]+=1
        for i in t:
            if(i not in s2):
                s2[i]=1
            else:
                s2[i]+=1
        return s1==s2
        