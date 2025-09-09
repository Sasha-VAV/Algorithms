from typing import List
from collections import defaultdict


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        users = defaultdict(int)
        for message, sender in zip(messages, senders):
            users[sender] += message.count(" ") + 1
        a, b = "-1", -1
        for k, v in users.items():
            if v > b:
                a = k
                b = v
            elif v == b:
                a = max(a, k)
        return a


if __name__ == "__main__":
    messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]
    senders = ["Alice",
                                                                                                            "userTwo",
                                                                                                            "userThree",
                                                                                                            "Alice"]
    print(Solution().largestWordCount(messages, senders))