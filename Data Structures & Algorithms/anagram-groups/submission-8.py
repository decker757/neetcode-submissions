class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sorted_strs = []
        hm = {}
        for word in strs:
            sorted_strs.append(",".join(sorted(word)))
        
        for i, word in enumerate(sorted_strs):
            if word not in hm:
                hm[word] = []
            hm[word].append(i)
        
        for v in hm.values():
            ls = []
            for i in range(len(v)):
                idx = v[i]
                ls.append(strs[idx])
            res.append(ls)
        
        return res

        
