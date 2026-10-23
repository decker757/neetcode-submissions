class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followerMap = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId, self.counter])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []

        self.followerMap[userId].add(userId)
        for followeeId in self.followerMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                tweetId, counter = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [counter, tweetId, followeeId, index - 1])
        
        while heap and len(res) < 10:
            counter, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                tweetId, counter = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [counter, tweetId, followeeId, index - 1])
        return res            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].discard(followeeId)
