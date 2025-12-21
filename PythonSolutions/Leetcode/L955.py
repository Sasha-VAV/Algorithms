from collections import defaultdict, deque


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        q = deque()
        q.appendleft([*range(len(strs))])
        res = 0
        for j in range(len(strs[0])):
            new_q = deque()
            backup_q = q.copy()
            while q:
                group = q.pop()
                if len(group) < 2: continue
                curr_group = [group[0]]
                for i in group[1:]:
                    if strs[curr_group[-1]][j] > strs[i][j]:
                        break
                    if strs[curr_group[-1]][j] == strs[i][j]:
                        curr_group.append(i)
                    else:
                        new_q.appendleft(curr_group)
                        curr_group = [i]
                else:
                    new_q.appendleft(curr_group)
                    continue
                res += 1
                new_q = backup_q
                break
            q = new_q
        return res


if __name__ == "__main__":
    arr = ["bwwdyeyfhc","bchpphbtkh","hmpudwfkpw","lqeoyqkqwe","riobghmpaa","stbheblgao","snlaewujlc","tqlzolljas","twdkexzvfx","wacnnhjdis"]
    print(Solution().minDeletionSize(arr))