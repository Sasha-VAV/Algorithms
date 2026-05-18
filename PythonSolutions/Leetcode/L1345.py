class Solution:
    def minJumps(self, arr: List[int]) -> int:
        new_arr = []
        prev = None
        count = 0
        for num in arr:
            if num != prev:
                new_arr.append(num)
                prev = num
                count = 0
            elif count < 2:                
                new_arr.append(num)
            count += 1
        arr = new_arr
        ref = defaultdict(list)
        for i, num in enumerate(arr):
            ref[num].append(i)
        
        q = deque()
        q.appendleft(0)
        res = 0
        visited = [False] * len(arr)
        visited[0] = True
        while True:
            new_q = deque()
            while q:
                i = q.pop()
                if i == len(arr) - 1:
                    return res
                for j in chain(ref[arr[i]], (i - 1, i + 1)):
                    if visited[j] or not (0 <= j < len(arr)):
                        continue
                    new_q.appendleft(j)
                    visited[j] = True
                ref.pop(arr[i])
            res += 1
            q = new_q
        raise NotImplementedError()