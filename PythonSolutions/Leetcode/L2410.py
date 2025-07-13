class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = len(players) - 1
        j = len(trainers) - 1
        res = 0
        while j >= 0:
            while i >= 0 and trainers[j] < players[i]:
                i -= 1
            if i == -1: return res
            res += 1
            i -= 1
            j -= 1
        return res