class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_s = []
        res = []
        hm = defaultdict(list)

        for s in strs:
            sorted_s.append("".join(sorted(s)))
        
        for i, s in enumerate(sorted_s):
            hm[s].append(strs[i])
        
        for k in hm:
            res.append(hm[k])

        return res
        
        