class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_ls = [0] * 26
        s2_ls = [0] * 26

        for i in range(len(s1)):
            s1_ls[ord(s1[i]) - ord('a')] += 1
            s2_ls[ord(s2[i]) - ord('a')] += 1 

        if s1_ls == s2_ls:
            return True        

        for i in range(len(s1), len(s2)):
            s2_ls[ord(s2[i]) - ord('a')] += 1
            s2_ls[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_ls == s2_ls:
                return True
                
        return False