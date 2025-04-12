import heapq
from collections import deque
from typing import List


class Twitter:

    def __init__(self):
        self.following = dict()
        self.posts = dict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId] = self.posts.get(userId, list()) + [(-self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following.get(userId, set())
        following.add(userId)
        posts = []
        for followee in following:
            posts.extend(self.posts.get(followee, []))
        heapq.heapify(posts)
        most_recent = heapq.nsmallest(10, posts)
        return [post for _, post in most_recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 10)
    twitter.postTweet(2, 20)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.follow(1, 2)
    print(twitter.getNewsFeed(1))
    print(twitter.getNewsFeed(2))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))