"""
user -> 
    all users that this user follows -> set of ID's that this user follows
    all tweets by this user -> list of tweet ID's that this user has posted
"""
from collections import defaultdict
from typing import List
from heapq import *

class Twitter:

    def __init__(self):
        self.userFollowing = defaultdict(list) # {1: [2, 3, 4]}
        self.userTweets = defaultdict(list) # {1: [t1, t2, t3]}
        self.tweets = []
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # print(self.userTweets)
        self.userTweets[userId].append((self.timer, tweetId))
        # print(self.userTweets)
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        alltweetheap = []
        following = self.userFollowing[userId][:]
        following.append(userId)
        # print(following)
        visited = set()
        for followeeId in following:
            for tweetTime, tweetId in self.userTweets[followeeId]:
                if tweetId in visited:
                    continue
                heappush(alltweetheap, (tweetTime, tweetId))
                visited.add(tweetId)
                if len(alltweetheap) > 10:
                    heappop(alltweetheap)
        alltweetheap.sort(reverse=True)
        return [i[1] for i in alltweetheap]


    def follow(self, followerId: int, followeeId: int) -> None:
        # print(self.userFollowing)
        self.userFollowing[followerId].append(followeeId)
        # print(self.userFollowing)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowing[followerId]:
            self.userFollowing[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)