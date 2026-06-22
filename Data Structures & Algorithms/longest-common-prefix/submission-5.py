class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        d={}
        for i in strs:
            s=""
            for x in i:
                s+=x
                if(s not in d):
                    d[s]=1
                else:
                    d[s]+=1
        s=""
        for i in d:
            if(d[i]==len(strs) and len(i)>=len(s)):  # <-- fix here
                s=i
        return s