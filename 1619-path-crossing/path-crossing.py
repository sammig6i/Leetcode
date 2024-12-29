class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direc = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }
        visited = set()
        x, y = 0, 0
        for c in path:
            visited.add((x, y))
            x += direc[c][0]
            y += direc[c][1]
            if (x, y) in visited:
                return True
        return False
