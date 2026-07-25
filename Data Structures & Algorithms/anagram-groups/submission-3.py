class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedArr = []
        res = []
        wordDict = {}
        for word in strs:
            sortedArr.append(sorted(word))

        for i in range(len(strs)):
            sortedWord = ",".join(sortedArr[i])
            print(sortedWord)
            if sortedWord not in wordDict:
                wordDict[sortedWord] = []
            wordDict[sortedWord].append(strs[i])
        
        for k in wordDict:
            res.append(wordDict[k])
        
        return res