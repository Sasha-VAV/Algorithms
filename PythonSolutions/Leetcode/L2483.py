class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_prefix = [0] * (len(customers) + 1)
        n_prefix = [0] * (len(customers) + 1)
        for i, c in enumerate(customers):
            y_prefix[i+1] = y_prefix[i]
            n_prefix[i+1] = n_prefix[i]
            if c == "Y":
                y_prefix[i+1] += 1
            else:
                n_prefix[i+1] += 1
        best_idx = 0
        best_penalty = y_prefix[-1] + n_prefix[-1] + 1
        for i, (yep, nope) in enumerate(zip(y_prefix, n_prefix)):
            if (tmp := nope + y_prefix[-1] - yep) < best_penalty:
                best_idx = i
                best_penalty = tmp
        # uncreachable
        return best_idx