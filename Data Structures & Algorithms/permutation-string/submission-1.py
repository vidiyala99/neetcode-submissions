class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1=[0]*26
        for i in s1:
            a1[ord(i)-97]+=1
        for i in range(len(s2)-len(s1)+1):
            a2=[0]*26
            temp=s2[i:i+len(s1)]
            for x in temp:
                a2[ord(x)-97]+=1
            if(a1==a2):
                return True
        return False
