class Solution:
    def isPathCrossing(self, path: str) -> bool:
        r, c = 0, 0
        visited = {(r, c)}
        direc = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for p in path:
            if p == "N":
                dr, dc = direc[2]
            elif p == "S":
                dr, dc = direc[0]
            elif p == "E":
                dr, dc = direc[1]
            elif p == "W":
                dr, dc = direc[3]
            r += dr
            c += dc
            if (r, c) in visited:
                return True
            visited.add((r, c))
        return False
