class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        def dfs(r, c):
            board[r][c] = "."

            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
            
                if 0 <= new_r < M and 0 <= new_c < N and board[new_r][new_c] == "X":
                    dfs(new_r, new_c)

        M = len(board)
        N = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        for r in range(M):
            for c in range(N):
                if board[r][c] == "X":
                    res += 1
                    dfs(r, c)
        
        return res
        
    