class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        N = len(grid)
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N 
                or grid[r][c]):
                continue
            elif r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visited:
                    visited.add((r + dr, c + dc))
                    q.append((r + dr, c + dc, length + 1))
        return -1