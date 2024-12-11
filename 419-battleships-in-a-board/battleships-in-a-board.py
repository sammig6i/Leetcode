class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        M = len(board)
        N = len(board[0])
        res = 0
        for r in range(M):
            for c in range(N):
                if board[r][c] == "X":
                    if ((r == 0 or board[r - 1][c] == ".") and
                    (c == 0 or board[r][c - 1] == ".")):
                        res += 1
        return res
        