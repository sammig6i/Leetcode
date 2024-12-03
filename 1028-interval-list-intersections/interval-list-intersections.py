class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        res = []

        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if start1 > end2:
                p2 += 1
            elif start2 > end1:
                p1 += 1
            else:
                res.append([max(start1, start2), min(end1, end2)])
                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1
        return res
    
# [0, 2] [5, 10] [13, 23] [24, 25]
# [1, 5] [8, 12] [15, 24] [25, 26]

# [1, 2] [5, 5] [8, 10] [15, 23] [24, 24] [25, 25]