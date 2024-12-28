class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        losses_count = defaultdict(int)

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            losses_count[loser] += 1
        
        one_loss = []
        zero_loss = []
        for player in seen:
            if player not in losses_count:
                zero_loss.append(player)
            elif losses_count[player] == 1:
                one_loss.append(player)
        return [sorted(zero_loss), sorted(one_loss)]

