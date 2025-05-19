class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums
        ab,bc,ac = a+b,b+c,a+c
        if a >= bc or b >= ac or c >= ab:
            return "none"
        if a == b and b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        return "scalene"