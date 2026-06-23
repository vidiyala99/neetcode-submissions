class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        i=0
        l=[]
        while(i<len(s)):
            j=i
            while(s[j]!="#"):
                j+=1
            le=int(s[i:j])
            l.append(s[j+1:j+1+le])
            i=j+1+le
        return l
