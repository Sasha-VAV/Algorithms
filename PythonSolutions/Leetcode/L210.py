from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [-1] * numCourses
        for a, b in prerequisites:
            if courses[a] == -1:
                courses[a] = [b]
            else:
                courses[a].append(b)

        possibles = set()
        visited_edges = set()
        edges = []
        def is_possible(course):
            if course in possibles:
                return True
            depends = courses[course]
            if depends == -1:
                possibles.add(course)
                edges.append(course)
                return True
            for dependant in depends:
                if (course, dependant) in visited_edges:
                    return False
                visited_edges.add((course, dependant))
                if not is_possible(dependant):
                    return False
            possibles.add(course)
            edges.append(course)
            return True

        for i in range(numCourses):
            if not is_possible(i):
                return []
        return edges


if __name__ == '__main__':
    print(Solution().findOrder(4, [[1,2],[2,0],[3,1],[3,2]]))