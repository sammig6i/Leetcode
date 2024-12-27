class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)

        for winner, loser in matches:
            loss_count[winner] = loss_count.get(winner, 0)
            loss_count[loser] += 1
            
        zero_loss = []
        one_loss = []
        for player, count in loss_count.items():
            if count == 0:
                zero_loss.append(player)
            elif count == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]
