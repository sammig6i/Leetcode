class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        starSet = set()

        for e in edges:
            for i in e:
                if i in starSet:
                    return i
                starSet.add(i)