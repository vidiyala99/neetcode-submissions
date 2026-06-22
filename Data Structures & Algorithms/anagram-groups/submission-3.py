class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1={}
        for i in strs:
            s="".join(sorted(i))
            if( s not in d1):
                d1[s]=[i]
            else:
                d1[s].append(i)
        l=[]
        for i in d1:
            l.append(d1[i])
        return l
