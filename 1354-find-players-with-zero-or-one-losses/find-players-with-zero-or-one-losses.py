class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)

        for winner, loser in matches:
            losses[winner] = losses.get(winner, 0)
            losses[loser] += 1
        
        zero_loss, one_loss = [], []
        for player, count in losses.items():
            if count == 0:
                zero_loss.append(player)
            elif count == 1:
                one_loss.append(player)
        
        return [sorted(zero_loss), sorted(one_loss)]