class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) #userid - [count, tweetids]
        self.count = 0
        self.followMap = defaultdict(set) #userid - set(followeeid)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 #to use minheap on count variable (lowest == most recent tweet)
        
    #the getNewsFeed portion i had to look up from the solution and couldnt figure out myself
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId) #his own tweets are supposed to show up as well
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap.keys():
                i = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][i]
                heapq.heappush(minheap, [count, tweetId, followeeId, i - 1]) 
                # the index - 1 is a helper to find the next recent tweet

        while minheap and len(res) < 10:
            count, tweetId, followeeId, i = heapq.heappop(minheap)
            res.append(tweetId)
            if i >= 0:
                count, tweetId = self.tweetMap[followeeId][i]
                heapq.heappush(minheap, [count, tweetId, followeeId, i - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
