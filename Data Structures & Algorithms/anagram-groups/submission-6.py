class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(w)) for w in strs]
        res = []
        d = defaultdict(list)

        for i in range(len(sorted_strs)):
            k, v = sorted_strs[i], strs[i]
            d[k].append(v)
        
        for k in d:
            res.append(d[k])
        
        return res