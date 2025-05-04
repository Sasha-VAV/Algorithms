class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        people = dict()
        for account in accounts:
            name = account[0]
            curr = set(account[1:])
            if name in people:
                x = -1
                arr = people[name]
                to_remove = []
                for i, emails in enumerate(arr):
                    if len(emails.intersection(curr)) > 0:
                        if x == -1:
                            arr[i] = emails.union(curr)
                            x = i
                        else:
                            arr[x] = emails.union(arr[x])
                            to_remove.append(i)
                if to_remove:
                    shift = 0
                    for rm in to_remove:
                        arr.pop(rm - shift)
                        shift += 1
                if x == -1:
                    people[name].append(curr)
            else:
                people[name] = [curr]
        res = []
        for name, person in people.items():
            for emails in person:
                res.append([name, *sorted(emails)])
        return res