class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,s2=[0]*26,[0]*26
        for i in s:
            s1[ord(i)-97]+=1
        for i in t:
            s2[ord(i)-97]+=1
        return s1==s2
        

        