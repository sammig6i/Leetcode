class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        loss_count = defaultdict(int)

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            loss_count[loser] += 1
        
        zero_loss = []
        one_loss = []
        for player in seen:
            if player not in loss_count:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        return [sorted(zero_loss), sorted(one_loss)]