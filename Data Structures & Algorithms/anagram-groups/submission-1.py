class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            
            if sorted_s not in freq:
                freq[sorted_s] = [s]
            else:
                freq[sorted_s].append(s)


        return list(freq.values()) 
