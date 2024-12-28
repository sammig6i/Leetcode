class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        losses_count = defaultdict(int)

        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] += 1
        
        one_loss = []
        zero_loss = []
        for player, losses in losses_count.items():
            if losses == 0:
                zero_loss.append(player)
            elif losses == 1:
                one_loss.append(player)
        return [sorted(zero_loss), sorted(one_loss)]

