class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        for s in strs:
            sorted_ch = sorted(s)
            sorted_word = "".join(sorted_ch)
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [s]
            else:
                hashmap[sorted_word].append(s)
        for key in hashmap:
            result.append(hashmap[key])
        return result

