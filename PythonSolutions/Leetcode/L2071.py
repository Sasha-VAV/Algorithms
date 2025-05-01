from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n = len(workers)
        def is_fit(k):
            if n - k < 0:
                return False
            n_pills = pills
            sorted_list = workers[n-k:]
            sorted_list.sort()
            for t in tasks[k-1::-1]:
                if sorted_list[-1] >= t:
                    sorted_list.pop()
                    continue
                elif n_pills == 0:
                    return False
                i = -1
                l = 0
                r = len(sorted_list) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if sorted_list[mid] + strength >= t:
                        i = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                if i == -1:
                    return False
                sorted_list.pop(i)
                n_pills -= 1
            return True

        l = 1
        r = len(tasks)
        max_tasks = 0
        while l <= r:
            mid = (l + r) // 2
            if is_fit(mid):
                max_tasks = mid
                l = mid + 1
            else:
                r = mid - 1
        return max_tasks


if __name__ == '__main__':
    tasks = [4,6,9,7,10,5,5]
    workers = [1,8,1,5,3,1,4,2,7]
    print(Solution().maxTaskAssign(tasks, workers, 1, 2))