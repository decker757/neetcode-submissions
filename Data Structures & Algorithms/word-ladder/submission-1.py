class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            What we know:
                when traversing the wordList, only 1 char can change at a time
                there's a chance that endWord doesn't exist in wordList
            
            Approach:
                - Check if endWord in wordList
                - Form a graph where we link the word in wordList to one another
                    - each node represents a word where root = beginWord
                    - then edges form between nodes such that there is a 1 char diff
                - BFS towards the endWord
        """

        if endWord not in wordList:
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                adjList[p].append(word)

        q = deque([beginWord])
        visited = {beginWord}
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    p = word[:i] + "*" + word[i+1:]
                    for nei in adjList[p]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0


