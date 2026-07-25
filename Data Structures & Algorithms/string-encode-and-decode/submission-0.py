class Solution:

    def encode(self, strs: List[str]) -> str:
        final_s = ""

        for s in strs:
            final_s += str(len(s)) + '#' + s
        
        return final_s
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res
