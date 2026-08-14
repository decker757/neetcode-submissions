class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1, hm2 = {}, {}
        l = 0

        if len(s1) > len(s2): return False

        for i in range(len(s1)):
            hm1[s1[i]] = 1 + hm1.get(s1[i], 0)
            hm2[s2[i]] = 1 + hm2.get(s2[i], 0)

        matches = 0

        for k in hm1:
            if hm1[k] == hm2.get(k, 0):
                matches += 1
        
        for r in range(len(s1), len(s2)):
            if len(hm1) == matches:
                return True

            ch = s2[r]
            hm2[ch] = 1 + hm2.get(ch, 0)

            if ch in hm1 and hm2[ch] == hm1[ch]:
                matches += 1
            elif ch in hm1 and hm1[ch] + 1 == hm2[ch]:
                matches -=1

            ch = s2[l]
            hm2[ch] -= 1
            if ch in hm1 and hm2[ch] == hm1[ch]:
                matches += 1
            elif ch in hm1 and hm1[ch] - 1 == hm2[ch]:
                matches -= 1
            
            l += 1

        return matches == len(hm1)