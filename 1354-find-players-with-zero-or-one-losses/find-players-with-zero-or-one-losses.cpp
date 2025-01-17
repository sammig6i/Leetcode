class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> losses;
        unordered_set<int> seen;
        for (auto match : matches) {
            int winner = match[0];
            int loser = match[1];

            seen.insert(winner);
            seen.insert(loser);
            
            losses[loser]++;
        }

        vector<int> zero_loss;
        vector<int> one_loss;
        for (auto player : seen) {
            if (losses.find(player) == losses.end()) {
                zero_loss.push_back(player);
            } else if (losses[player] == 1) {
                one_loss.push_back(player);
            }
        }

        sort(zero_loss.begin(), zero_loss.end());
        sort(one_loss.begin(), one_loss.end());
        return {zero_loss, one_loss};
    }
};