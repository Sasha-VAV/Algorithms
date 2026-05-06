class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        heap = set()
        num_start = {}
        num_end = {}
        used = set()

        for num in nums:
            if num in used:
                continue
            used.add(num)
            if num + 1 in num_start:
                _, end = num_start[num + 1]
                heap.remove(num_start[num + 1])
                num_start.pop(num + 1)
                if num in num_end:
                    start, _ = num_end[num]
                    heap.remove(num_end[num])
                else:
                    start = num
                
            elif num in num_end:
                start, _ = num_end[num]
                heap.remove(num_end[num])
                num_end.pop(num)
                if num in num_start:
                    _, end = num_start[num]
                    heap.remove(num_start[num])
                else:
                    end = num + 1
                
            else:
                start = num
                end = num + 1
            
            new_value = (start, end)
            heap.add(new_value)
            num_start[start] = new_value
            num_end[end] = new_value
        
        res = 0
        for start, end in heap:
            res = max(res, end - start)
        return res
    

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))