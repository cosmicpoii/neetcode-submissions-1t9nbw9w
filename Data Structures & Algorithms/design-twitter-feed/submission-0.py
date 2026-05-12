class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> list of [time, tweetId]
        self.followMap = defaultdict(set) # followerId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            for time, tweetId in self.tweetMap[followeeId]:
                heapq.heappush(heap, [-time, tweetId])

        while heap and len(res) < 10:
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
