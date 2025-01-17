class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> losses;
        for (auto match : matches) {
            int winner = match[0];
            int loser = match[1];

            losses[loser]++;
            losses[winner] += 0;
        }

        vector<int> no_loss;
        vector<int> one_loss;
        for (const auto& [player, count] : losses) {
            if (count == 0) {
                no_loss.push_back(player);
            } else if (count == 1) {
                one_loss.push_back(player);
            }
        }

        sort(no_loss.begin(), no_loss.end());
        sort(one_loss.begin(), one_loss.end());
        return {no_loss, one_loss};
    }
};