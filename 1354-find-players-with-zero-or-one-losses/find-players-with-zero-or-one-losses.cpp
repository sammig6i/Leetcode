class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> losses;
        for (auto match : matches) {
            int winner = match[0];
            int loser = match[1];

            losses[winner] += 0;
            losses[loser]++;
        }

       vector<vector<int>> res(2);
        for (auto [player, count] : losses) {
            if (!count) {
                res[0].push_back(player);
            } else if (count == 1) {
                res[1].push_back(player);
            }
        }

        for (auto& arr : res) {
            sort(arr.begin(), arr.end());
        }

        return {res[0], res[1]};
    }

};