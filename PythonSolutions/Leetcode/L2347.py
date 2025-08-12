from typing import List
from collections import Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits.count(suits[0]) == 5: return "Flush"
        counter = Counter(ranks)
        match max(counter.values()):
            case 4: return "Three of a Kind"
            case 3: return "Three of a Kind"
            case 2: return "Pair"
            case 1: return "High Card"
        return "Not allowed"